## 🧩 학습 목표

| 구분 | 내용 |
|------|------|
| **학습목표** | - Kafka CLI를 이용하여 다중 토픽을 생성할 수 있습니다.<br>- 각 토픽에 대해 프로듀서를 실행하고 메시지를 전송할 수 있습니다.<br>- 컨슈머를 실행하여 특정 토픽의 메시지를 수신할 수 있습니다. |
| **학습 개념** | Kafka에서 **토픽(Topic)** 은 메시지를 전달하는 핵심 요소입니다.<br>각 토픽은 독립적인 메시지 스트림을 가지며, 서로 다른 토픽에서 데이터를 분리하여 관리할 수 있습니다.<br>본 실습에서는 다중 토픽을 생성하고, 각 토픽에 메시지를 송수신하며 **Kafka의 메시지 분배 방식**을 학습합니다. |

---

## 🧭 학습 방향

김싸피는 여러 개의 Kafka 토픽을 생성하고, 각 토픽에 대해 메시지 송수신 테스트를 수행한 뒤, 컨슈머를 실행하여 특정 토픽의 메시지를 확인합니다.

### 수행 단계
- ✅ 다중 토픽 생성  
- ✅ 각 토픽에 대해 메시지 송수신 테스트  
- ✅ 컨슈머를 실행하여 특정 토픽의 메시지 확인  

---

## 📋 요구사항

### 1️⃣ 다중 토픽 생성

두 개의 토픽(`topic-1`, `topic-2`)을 생성합니다.

```bash
# topic-1 생성
bin/kafka-topics.sh --create --topic topic-1 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

# topic-2 생성
bin/kafka-topics.sh --create --topic topic-2 --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
```

2️⃣ 각 토픽에 메시지 송수신 테스트\
📤 Topic-1 메시지 전송 \
`bin/kafka-console-producer.sh --topic topic-1 --bootstrap-server localhost:9092`


입력:
Message to topic-1
Another message for topic-1

📤 Topic-2 메시지 전송\
`bin/kafka-console-producer.sh --topic topic-2 --bootstrap-server localhost:9092`

입력:
Message to topic-2
Another message for topic-2

3️⃣ 컨슈머 실행 및 특정 토픽 메시지 확인\
📥 Topic-1 메시지 소비\
`bin/kafka-console-consumer.sh --topic topic-1 --from-beginning --bootstrap-server localhost:9092`


Topic-1의 메시지가 정상적으로 출력되는지 확인합니다.

실행 결과를 캡쳐하여 제출하세요.

📥 Topic-2 메시지 소비\
`bin/kafka-console-consumer.sh --topic topic-2 --from-beginning --bootstrap-server localhost:9092`


Topic-2의 메시지가 정상적으로 출력되는지 확인합니다.

실행 결과를 캡쳐하여 제출하세요.