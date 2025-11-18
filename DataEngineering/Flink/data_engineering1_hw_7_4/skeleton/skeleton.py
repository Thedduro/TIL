import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # 환경 생성 Flink의 실행 환경을 설정하세요.
    env = StreamExecutionEnvironment.get_execution_environment()

    # 병렬성 조정 병렬성을 2로 설정하세요.
    env.set_parallelism(2)

    # CSV 파일 읽기
    df = pd.read_csv("../data/data.csv")

    # 필요한 컬럼만 선택 후 결측값 제거 (transaction_type과 amount 컬럼을 선택하고, 결측값을 제거하세요.)
    transactions = df[["transaction_type", "amount"]].dropna().values.tolist()

    # 데이터 스트림 생성 (데이터 타입 [문자열, 실수형]으로 지정하세요.)
    transaction_stream = env.from_collection(transactions, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))

    # 거래 유형별 총 거래 금액 계산
    transaction_total = (transaction_stream
                         .key_by(lambda x: x[0])
                         .reduce(lambda a, b: (a[0], a[1] + b[1])))

    # 결과 출력
    transaction_total.print()

    # 실행 (Flink 실행 함수를 작성해주세요.)
    env.execute("Transaction Type Aggregation")

if __name__ == "__main__":
    main()
