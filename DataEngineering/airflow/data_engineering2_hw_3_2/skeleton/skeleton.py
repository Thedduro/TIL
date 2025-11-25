from airflow import DAG  # DAG 생성을 위한 기본 클래스
from airflow.operators.empty import EmptyOperator  # 실행할 작업이 없는 "빈" 태스크
import pendulum  # 시간대 설정을 위한 라이브러리 (Airflow에서는 pendulum 사용)

# DAG 정의 (스케줄 없이 가장 기본적인 형태)
with DAG(
    dag_id="airflow3_2",  # DAG의 고유한 이름 (Airflow UI에서 보임)
    start_date=pendulum.today("Asia/Seoul"),  # DAG의 시작 날짜 (오늘 날짜)
) as dag:

    # DAG 안에서 실행할 태스크(Task) 정의
    # _____ 는 실제 실행할 작업이 없는 "빈" 태스크를 의미함
    start = EmptyOperator(task_id="start")  # 시작 지점 역할
    end = EmptyOperator(task_id="end")  # 끝 지점 역할

    # 실행 순서 지정 (start → end 순서로 실행)
    start >> end  
