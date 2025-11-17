"""
Kafka Exporter를 활용하여 특정 컨슈머 그룹의 Lag을 모니터링하는 스크립트입니다.

TODO:
1. Prometheus API를 호출하여 특정 컨슈머 그룹의 모든 파티션 Lag 합계를 가져옵니다.
2. 일정 주기(예: 5초)마다 Lag을 출력합니다.
3. Lag 값이 특정 임계값(예: 100 이상)을 초과하면 경고 메시지를 출력합니다.
"""

import time
import requests

# 설정 값
PROMETHEUS_URL = "http://localhost:9308/metrics"  # Kafka Exporter가 실행 중인 주소
CONSUMER_GROUP = 'mygroup'  # 모니터링할 컨슈머 그룹명
LAG_THRESHOLD = 100  # Lag이 초과할 경우 경고를 출력할 임계값
CHECK_INTERVAL = 5  # Lag 확인 주기(초 단위)

# 1. Prometheus API를 호출하여 특정 컨슈머 그룹의 모든 파티션 Lag 합계를 반환하는 함수
def get_consumer_lag():
    response = requests.get(PROMETHEUS_URL)
    lines = response.text.split('\n')
    total_lag = 0
    for line in lines:
        if f'kafka_consumergroup_lag{{consumergroup="{CONSUMER_GROUP}"' in line:
            lag_value = float(line.split()[-1])
            total_lag += lag_value
    return total_lag  # 모든 파티션의 Lag 합 반환

while True:
    lag = get_consumer_lag()
    print(f"Current Lag for {CONSUMER_GROUP}: {lag}")

    # 2.Lag이 임계값 이상이면 경고 메시지를 출력
    if lag >= LAG_THRESHOLD:
        print("WARNING: Consumer Lag is too high!")

    time.sleep(CHECK_INTERVAL)  # 3. 일정 주기마다 Lag을 체크하세요.