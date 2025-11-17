import pandas as pd
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.typeinfo import Types

def main():
    # 환경 생성 (Flink의 실행 환경을 설정하세요.)
    env = StreamExecutionEnvironment.get_execution_environment()

    # 병렬성 조정 (병렬성을 2로 설정하세요.)
    env.set_parallelism(2)

    # CSV 파일 읽기
    df = pd.read_csv("../data/data.csv")

    # news_text 컬럼에서 결측값 제거 후 리스트 변환 (news_text 컬럼을 선택하세요.)
    news_texts = df["news_text"].dropna().tolist()

    # 데이터 스트림 생성 (문자열 데이터 타입을 지정하세요.)
    text_stream = env.from_collection(news_texts, type_info=Types.STRING())

    # WordCount 파이프라인 구성
    word_count = (text_stream
                  .map(lambda text: [(word.lower(), 1) for word in text.split()], output_type=Types.LIST(Types.TUPLE([Types.STRING(), Types.INT()])))
                  .flat_map(lambda words: words, output_type=Types.TUPLE([Types.STRING(), Types.INT()]))
                  .key_by(lambda x: x[0])
                  .reduce(lambda a, b: (a[0], a[1] + b[1])))

    # 결과 출력(출력함수를 작성하세요.)
    word_count.print()

    # 실행
    env.execute("Finance News WordCount")

if __name__ == "__main__":
    main()
