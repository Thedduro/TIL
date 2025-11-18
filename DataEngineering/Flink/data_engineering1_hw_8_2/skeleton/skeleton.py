import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # Flink 스트리밍 실행 환경 설정
    env = StreamExecutionEnvironment.get_execution_environment()  # Flink 실행 환경을 가져오는 함수 호출

    # CSV 데이터 불러오기
    df = pd.read_csv("../data/data.csv")
    transactions = df[["transaction_type", "amount"]].dropna().values.tolist()  

    # 스트리밍 데이터 스트림 생성
    transaction_stream = env.from_collection(transactions, type_info=Types.TUPLE([Types.STRING(), Types.FLOAT()]))  # 데이터 스트림을 생성하는 메서드(문자열, 실수로 이루어진 튜플 정의)

    # 거래 유형별 금액 합산 파이프라인 구성
    total_amount_per_type = (transaction_stream
                             .key_by(lambda x: x[0])  # 거래 유형(transaction_type, x[0]) 기준 그룹화
                             .sum(1))  # 합산할 컬럼 인덱스 입력

    # 결과 실시간 출력
    total_amount_per_type.print()

    # 실행
    env.execute("Streaming Transaction Processing")  # Flink 실행을 시작하는 메서드 호출

if __name__ == "__main__":
    main()
