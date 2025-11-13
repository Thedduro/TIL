# Kafka 모니터링 대시보드 구축 실습 README  
**Grafana + Prometheus + Kafka(JMX Exporter) 실시간 모니터링**

---

## 📌 1. 실습 목표

### ✔ 학습 목표
- Kafka의 주요 메트릭(CPU, 메모리, GC, 메시지 수신량, 바이트 입출력량 등)을 실시간으로 시각화할 수 있다.
- Grafana 공식 Kafka Dashboard(ID: 721)를 Import하여 주요 지표를 분석할 수 있다.
- Prometheus와 JMX Exporter를 활용해 Kafka JMX 메트릭을 수집하는 과정을 이해한다.

### ✔ 학습 개념
Kafka는 대규모 메시지 스트림 처리 시스템으로 **실시간 모니터링**이 매우 중요하다.  
Grafana + Prometheus 구성을 통해 Kafka Broker의 성능을 모니터링할 수 있으며,  
특히 Dashboard ID **721**은 Kafka 주요 지표 분석에 널리 사용되는 공식 템플릿이다.

---

## 📌 2. 실습 요구사항

### (1) Grafana 설치 및 실행

WSL에서 다음 명령어 실행:

```bash
wget https://dl.grafana.com/oss/release/grafana-10.2.2.linux-amd64.tar.gz
tar -xvzf grafana-10.2.2.linux-amd64.tar.gz
cd grafana-10.2.2
./bin/grafana-server
```

-  브라우저 접속:
    - 주소: http://localhost:3000
    - 로그인: admin / admin

### 2. Prometheus 데이터 소스 추가
Grafana UI에서 Connections → Data Sources로 이동합니다."Add data source" 버튼을 클릭하고 Prometheus를 선택합니다.URL을 http://localhost:9090으로 설정한 후 Save & Test를 클릭하여 연결을 확인합니다.

### 3. Kafka 모니터링 대시보드
ImportGrafana UI 상단 메뉴에서 + → Import로 이동합니다.Dashboard ID: 721을 입력하고 Load 버튼을 클릭합니다.(링크 : https://grafana.com/grafana/dashboards/721-kafka/)데이터 소스로 Prometheus를 선택하고 Import를 클릭합니다.

### 4. 주요 메트릭 확인 및 분석
Import된 대시보드에서는 다음과 같은 Kafka 주요 메트릭이 시각화되어 있어야 합니다. 
CPU Usage\JVM Memory Used\Time spent in GC\Messages In per Topic\Bytes In per Topic\Bytes Out per Topic\

### 5. 진행시 유의사항
-  메시지 전송 필수 다음 메트릭은 Kafka에 메시지가 실제로 전송되어야만 시각화 패널에 데이터가 나타납니다. 
    - Messages In per Topic
    - Bytes In per Topic- Bytes Out per Topic 따라서 실습 중에는 kafka-console-producer.sh를 활용하여 테스트 메시지를 반드시 전송해 보세요. 
- 쿼리 수정 필요성 공식 대시보드가 업데이트된 지 다소 시간이 지나, 일부 패널에서는 메트릭이 비정상적으로 표시되거나 사라지는 경우가 있습니다. 이럴 경우, 다음과 같은 쿼리로 수정하면 보다 안정적으로 메트릭이 표시됩니다: 
    - sum by(topic) (kafka_server_BrokerTopicMetrics_OneMinuteRate{name="MessagesInPerSec"}) 
    - sum by(topic) (kafka_server_BrokerTopicMetrics_OneMinuteRate{name="BytesInPerSec"}) 
    - sum by(topic) (kafka_server_BrokerTopicMetrics_OneMinuteRate{name="BytesOutPerSec"})

수정된 쿼리는 토픽별 합계(sum by topic) 방식으로 데이터를 그룹화하여 시각화합니다.왜 이 방식이어야 진행이 되는지, 어떤 변화가 있었는지 한번 확인해보세요.