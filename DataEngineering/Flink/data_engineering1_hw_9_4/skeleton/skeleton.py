import json
import os
from datetime import datetime

from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.connectors import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.common.typeinfo import Types
from pyflink.datastream.window import TumblingProcessingTimeWindows
from pyflink.common.time import Time
from pyflink.datastream.functions import AggregateFunction
from pyflink.common import Configuration


# ---------------------------------------------------------------------
# 사용자 정의 집계 함수(AggregateFunction)
# 동일한 sensor_id의 데이터를 일정 시간 간격(윈도우)으로 모아
# 평균 온도, 평균 습도, 마지막 상태 등을 계산함
# ---------------------------------------------------------------------
class SensorAggregate(AggregateFunction):
    def create_accumulator(self):
        """
        누적기(accumulator)를 초기화.
        튜플 형태로 반환하며, 순서는 다음과 같음:
        (온도 합계, 습도 합계, 데이터 개수, 마지막 상태, 센서 ID)
        """
        return (0.0, 0.0, 0, "", "")

    def add(self, value, accumulator):
        """
        새로 들어온 데이터를 기존 누적기에 더함.
        value는 아래 형태의 튜플임:
        (sensor_id, location, temperature, humidity, status)
        """
        temp_sum, humid_sum, count, _, _ = accumulator
        return (
            temp_sum + value[2],    # 온도 누적
            humid_sum + value[3],   # 습도 누적
            count + 1,              # 데이터 개수 증가
            value[4],               # 마지막 상태 갱신
            value[0],               # 센서 ID 유지
        )

    def get_result(self, accumulator):
        """
        윈도우가 닫힐 때 최종 집계 결과를 반환.
        JSON 문자열로 변환하여 출력 또는 Kafka 전송에 사용함.
        """
        temp_sum, humid_sum, count, last_status, sensor_id = accumulator
        return json.dumps({
            "sensor_id": sensor_id,
            "avg_temperature": round(temp_sum / count, 2),
            "avg_humidity": round(humid_sum / count, 2),
            "last_status": last_status,
            "update_time": datetime.utcnow().isoformat()  # UTC 시각 기준
        })

    def merge(self, acc1, acc2):
        """
        병렬 실행 시 여러 누적기를 합칠 때 사용됨.
        현재는 병렬성이 1이므로 실질적으로 사용되지 않음.
        """
        return acc1


# ---------------------------------------------------------------------
# JSON 문자열을 안전하게 파싱하는 함수
# 잘못된 형식의 메시지가 들어올 경우 예외 발생을 방지함
# ---------------------------------------------------------------------
def safe_json_parse(x):
    try:
        parsed = json.loads(x)
        print("[PARSE OK]", parsed)
        return parsed
    except Exception as e:
        print("[PARSE FAIL]", x, "| Error:", e)
        return {}  # 파싱 실패 시 빈 dict 반환


def main():
    # -----------------------------------------------------------------
    # 1. Flink-Kafka 커넥터 JAR 파일 등록
    # PyFlink는 Java 기반이므로, 외부 커넥터를 사용하기 위해
    # 해당 JAR 파일을 파이프라인 설정에 포함시켜야 함.
    # -----------------------------------------------------------------
    kafka_jar_path = os.path.abspath("flink-sql-connector-kafka-3.3.0-1.19.jar")
    config = Configuration()
    config.set_string("pipeline.jars", f"file://{kafka_jar_path}")

    # -----------------------------------------------------------------
    # 2. Flink 스트림 실행 환경(StreamExecutionEnvironment) 생성
    # 전체 스트리밍 파이프라인의 진입점이며,
    # 병렬 처리 수준(parallelism)을 설정할 수 있음.
    # -----------------------------------------------------------------
    env = StreamExecutionEnvironment.get_execution_environment(configuration=config)
    env.set_parallelism(1)

    # -----------------------------------------------------------------
    # 3. Kafka Consumer 생성
    # Kafka의 'sensor_readings' 토픽에서 데이터를 실시간으로 읽어옴.
    # 메시지는 문자열(JSON) 형식으로 역직렬화됨.
    # -----------------------------------------------------------------
    kafka_source = FlinkKafkaConsumer(
        topics='sensor_readings',
        deserialization_schema=SimpleStringSchema(),
        properties={
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'flink-sensor-group',
            'auto.offset.reset': 'earliest'  # 가장 처음 메시지부터 읽음
        }
    )

    # -----------------------------------------------------------------
    # 4. Kafka Producer 생성
    # 결과를 'sensor_stats' 토픽으로 다시 전송하기 위한 Sink 정의.
    # 집계된 평균값을 문자열(JSON)로 직렬화하여 전송함.
    # -----------------------------------------------------------------
    kafka_sink = FlinkKafkaProducer(
        topic='sensor_stats',
        serialization_schema=SimpleStringSchema(),
        producer_config={'bootstrap.servers': 'localhost:9092'}
    )

    # -----------------------------------------------------------------
    # 5. 데이터 스트림 구성 단계
    # - Kafka에서 읽은 JSON 문자열을 파싱
    # - 필요한 필드를 추출하여 튜플 형태로 변환
    # -----------------------------------------------------------------
    stream = env.add_source(kafka_source) \
        .map(lambda x: safe_json_parse(x), output_type=Types.MAP(Types.STRING(), Types.STRING())) \
        .map(lambda x: (
            x.get('sensor_id', 'unknown'),
            x.get('location', 'unknown'),
            float(x.get('temperature', 0.0)),
            float(x.get('humidity', 0.0)),
            x.get('status', 'UNKNOWN')
        ), output_type=Types.TUPLE([
            Types.STRING(),
            Types.STRING(),
            Types.FLOAT(),
            Types.FLOAT(),
            Types.STRING()
        ]))

    # -----------------------------------------------------------------
    # 6. 윈도우 기반 집계 로직
    # - key_by: sensor_id를 기준으로 데이터 그룹화
    # - window: 10초 단위의 Tumbling Window 생성
    #   (Processing Time 기준으로 일정 시간 단위로 데이터를 집계)
    # - aggregate: 사용자 정의 SensorAggregate 함수를 적용
    # 센서 ID를 기준으로 데이터를 그룹화한 후,센서 데이터를 집계하려면 동일한 센서에서 발생한 데이터끼리 그룹핑해야 하므로, 각 요소의 sensor_id를 기준으로 데이터를 묶어야 합니다.
    # sensor_id는 튜플의 첫 번째 요소에 위치하므로, key_by 함수에서 이를 기준으로 그룹핑하도록 구현합니다.
    # 이후 집계를 위한 시간 단위를 설정해야 하는데, 해당 스트리밍 처리에서는 실시간 처리 기준의 10초 단위로 데이터를 구분하여 집계합니다.
    # 따라서 Processing Time 기반의 고정 간격 윈도우(Tumbling Window)를 사용하고, 그 간격을 10초로 설정해 데이터를 시간 블록 단위로 분할해 처리할 수 있도록 구현합니다.
 
    # -----------------------------------------------------------------
    result_stream = stream \
        .key_by(lambda x: x[0]) \
        .window(TumblingProcessingTimeWindows.of(Time.seconds(10))) \
        .aggregate(SensorAggregate(), output_type=Types.STRING())

    # -----------------------------------------------------------------
    # 7. 결과 Sink 설정
    # - Kafka Sink로 전송
    # - print()를 통해 콘솔 출력 (테스트용)
    # -----------------------------------------------------------------
    result_stream.add_sink(kafka_sink)
    result_stream.print()

    # -----------------------------------------------------------------
    # 8. 스트리밍 잡 실행
    # Flink 엔진이 위에서 정의한 파이프라인을 실행하도록 명령
    # -----------------------------------------------------------------
    env.execute("Sensor Aggregation Stream Job")


# ---------------------------------------------------------------------
# 엔트리 포인트
# Python 스크립트로 실행될 때 main()을 호출
# ---------------------------------------------------------------------
if __name__ == '__main__':
    main()
