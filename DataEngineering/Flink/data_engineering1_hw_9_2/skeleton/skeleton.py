import pandas as pd
from datetime import datetime
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy, TimestampAssigner
from pyflink.datastream.window import TumblingEventTimeWindows
from pyflink.common import Duration, Time
from pyflink.common.typeinfo import Types
from pyflink.datastream.functions import AggregateFunction


# 사용자 정의 TimestampAssigner: 타임스탬프 필드 추출
class CustomTimestampAssigner(TimestampAssigner):
    def extract_timestamp(self, element, record_timestamp):
        return element[1]  # 데이터의 element 2번쨰 필드에서 타임스탬프를 추출


# 사용자 정의 AggregateFunction (평균 계산)
class AverageAggregate(AggregateFunction):
    def create_accumulator(self):
        """ 초기값 설정 (합계, 개수) """
        return (0.0, 0)

    def add(self, value, accumulator):
        """ 데이터를 누적하여 합계와 개수 증가 """
        return (accumulator[0] + value[2], accumulator[1] + 1)

    def get_result(self, accumulator):
        """ 최종 평균 계산 """
        return accumulator[0] / accumulator[1] if accumulator[1] > 0 else 0

    def merge(self, acc1, acc2):
        """ 병합 로직 (병렬 처리 시) """
        return (acc1[0] + acc2[0], acc1[1] + acc2[1])


def main():
    # Flink 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(2)  # 데이터 병렬 처리를 위해 병렬성을 설정

    # CSV 데이터 로드
    df = pd.read_csv("../data/data.csv")

    # 거래 ID, 타임스탬프, 금액 데이터 추출
    transactions = df[['transaction_id', 'timestamp', 'amount']].dropna().values.tolist()

    # 타임스탬프 변환 (밀리초 단위)
    transactions = [(str(t[0]), int(datetime.strptime(t[1], "%Y-%m-%d %H:%M:%S").timestamp() * 1000), float(t[2])) for t in transactions]

    # Flink 데이터 스트림 생성
    source = env.from_collection(
        transactions,
        type_info=Types.TUPLE([Types.STRING(), Types.LONG(), Types.FLOAT()])
    )

    # 워터마크 전략 설정
    watermark_strategy = (
        WatermarkStrategy.for_bounded_out_of_orderness(Duration.of_seconds(1))   # 워터마크 전략을 위한 메서드 입력
        .with_timestamp_assigner(CustomTimestampAssigner())
    )

    # 타임스탬프 및 워터마크 할당
    watermarked_stream = source.assign_timestamps_and_watermarks(watermark_strategy) # 워터마크 전략 적용

    # Tumbling 윈도우에서 평균 계산
    avg_window_stream = (
        watermarked_stream
        .key_by(lambda x: x[0])
        .window(TumblingEventTimeWindows.of(Time.seconds(5)))
        .aggregate(AverageAggregate())  # 사용자 정의 AggregateFunction 사용
    )

    # 결과 출력
    avg_window_stream.print("Tumbling Window Avg")

    # 실행
    env.execute("Tumbling Window Average Calculation")


if __name__ == "__main__":
    main()
