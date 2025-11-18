
from pyflink.table import EnvironmentSettings, TableEnvironment
import tempfile
import os
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Flink 배치 처리 시작")

    env_settings = EnvironmentSettings.in_batch_mode()
    table_env = TableEnvironment.create(env_settings)

    config = table_env.get_config().get_configuration()
    config.set_string("parallelism.default", "1")

    input_path = create_sample_csv()
    output_dir = tempfile.gettempdir() + '/flink_finance_output'

    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)

    # 빈칸: 소스 테이블 정의
    source_ddl = f"""
CREATE TABLE finance (
    stock_code STRING,
    sector STRING,
    price DOUBLE,
    volume INT,
    transaction_date STRING
) WITH (
    'connector' = 'filesystem',
    'path' = '{input_path}',
    'format' = 'csv'
)"""
    table_env.execute_sql(source_ddl)

    # 빈칸: 싱크 테이블 정의
    sink_ddl = f"""
CREATE TABLE finance_summary (
    sector STRING,
    total_value DOUBLE,
    avg_price DOUBLE,
    total_volume INT,
    transaction_count  BIGINT
) WITH (
    'connector' = 'filesystem',
    'path' = '{output_dir}',
    'format' = 'csv'
)
"""
    table_env.execute_sql(sink_ddl)

    # 빈칸: SQL 쿼리 작성 및 실행
    result = table_env.execute_sql("""
SELECT
    sector,
    SUM(price * volume) AS total_value,
    AVG(price) AS avg_price,
    SUM(volume) AS total_volume,
    COUNT(*) AS transaction_count
FROM finance
GROUP BY sector
""")


    print("\n=== 섹터별 금융 데이터 요약 ===")
    print("섹터\t총 거래액\t평균 가격\t총 거래량\t거래 건수")
    print("-" * 80)

    with result.collect() as results:
        for row in results:
            print(f"{row[0]}\t{row[1]:,.2f}\t{row[2]:,.2f}\t{row[3]:,}\t{row[4]:,}")

def create_sample_csv():
    temp_file = tempfile.gettempdir() + '/finance_data.csv'
    np.random.seed(42)
    stock_codes = ['005930', '000660', '035420', '068270']
    sectors = ['semiconductor', 'biotech', 'internet']

    data = []
    for _ in range(1000):
        stock_code = np.random.choice(stock_codes)
        sector = np.random.choice(sectors)
        price = round(np.random.uniform(50000, 1000000), 2)
        volume = np.random.randint(10, 1000)
        date = f"2025-{np.random.randint(1, 13):02d}-{np.random.randint(1, 29):02d}"
        data.append(f"{stock_code},{sector},{price},{volume},{date}")

    with open(temp_file, 'w') as f:
        f.write('\n'.join(data))

    return temp_file

if __name__ == '__main__':
    main()
