from airflow import DAG
import pendulum
from airflow.operators.python import PythonOperator

# 실행할 Python 함수 정의
def print_hello():
    print("Hello, Airflow!")  # 실행 시 "Hello, Airflow!" 메시지를 출력

# DAG (Directed Acyclic Graph) 정의
with DAG(
    dag_id="airflow3_4",  # DAG의 고유한 식별자
    schedule_interval="@once",  # DAG이 활성화될 때 한 번 실행
    start_date=pendulum.datetime(2025, 11, 25),  # 최신 날짜로 설정
    catchup=False,  # 과거 실행 방지 여부
) as dag:
    
    # PythonOperator를 사용한 Task 정의
    hello_task = PythonOperator(
        task_id='hello_task',  # Task의 고유한 ID
        python_callable=print_hello,  # 실행할 Python 함수 지정
        dag=dag  # DAG 객체 연결 (명확하게 지정)
    )
    
    # Task 실행 흐름 정의
    hello_task  # 단일 Task 실행
