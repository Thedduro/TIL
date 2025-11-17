## 🧩 학습 목표

| 구분 | 내용 |
|------|------|
| **학습목표** | - Kafka의 파티션 분배 원리를 이해한다.<br>- 특정 파티션에 메시지를 전송하는 키 기반 메시지 전송 방식을 학습한다.<br>- 특정 키를 사용하여 특정 파티션으로 메시지를 전송하는 방법을 실습한다. |
| **학습 개념** | Kafka의 메시지는 **파티션(Partition)** 단위로 저장됩니다.<br>Kafka는 **키가 있는 메시지**의 경우, 동일한 키를 가진 메시지가 항상 같은 파티션에 저장되도록 설계되어 있습니다.<br>본 실습에서는 특정 키를 사용하여 특정 파티션에만 메시지를 저장하는 방법을 학습하고, **키가 없는 메시지와 비교**하여 Kafka의 파티션 분배 방식을 실습합니다. |

---

## 🧭 학습 방향

김싸피는 Kafka 실행 상태를 확인하고 여러 개의 파티션을 가진 토픽을 생성한 뒤,  
특정 키를 사용하여 메시지를 전송하고 키 없이 전송한 경우의 동작을 비교하며,  
컨슈머를 실행해 특정 파티션에 메시지가 정상적으로 저장되었는지와  
다른 파티션에는 메시지가 없는지를 검증합니다.

### 수행 단계
- ✅ Kafka 실행 및 토픽 생성  
- ✅ 특정 키를 사용하여 메시지 전송  
- ✅ 컨슈머 실행 후 메시지 확인  

---

## 📋 요구사항

### 1️⃣ Kafka 실행 및 토픽 생성

Kafka 실행 여부를 확인한 뒤, **3개의 파티션을 가진 토픽을 생성**합니다.


```bash
# 토픽 생성 (3개의 파티션)
bin/kafka-topics.sh --create \
  --topic 3partitions-topic \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```
# 생성된 토픽 확인
`bin/kafka-topics.sh --list --bootstrap-server localhost:9092`
# 파티션 정보 확인
`bin/kafka-topics.sh --describe --topic 3partitions-topic --bootstrap-server localhost:9092`

```bash
# 키 기반 메시지 전송
bin/kafka-console-producer.sh --topic 3partitions-topic --bootstrap-server localhost:9092 \
  --property "parse.key=true" --property "key.separator=:"
```
▶️ 입력 예시\
key1:Hello from key1\
key1:Another message from key1\
key2:Hello from key2\
key3:Hello from key3\
- parse.key=true → : 왼쪽을 메시지 키로 인식
- key.separator=: → : 구분자로 키와 메시지 분리
- 같은 키(key1)는 항상 동일한 파티션으로 전송됨 ✅

```bash
# 파티션 / 키 정보와 함께 메시지 확인
bin/kafka-console-consumer.sh --topic 3partitions-topic \
  --bootstrap-server localhost:9092 \
  --from-beginning \
  --property print.key=true \
  --property print.partition=true
```
```bash
# 키 없이 메시지 전송
bin/kafka-console-producer.sh --topic 3partitions-topic --bootstrap-server localhost:9092

# 다시 컨슈머로 확인
bin/kafka-console-consumer.sh --topic 3partitions-topic \
  --bootstrap-server localhost:9092 \
  --from-beginning \
  --property print.key=true \
  --property print.partition=true
```

| 구분           | 동작 방식                                  | 결과                              |
| ------------ | -------------------------------------- | ------------------------------- |
| **키 지정 메시지** | 동일한 키 → 항상 동일한 파티션                     | 예: `key1`, `key2` → Partition 2 |
| **키 없는 메시지** | Round-Robin 분배 (단, 세션 단위로 한쪽에 몰릴 수 있음) | 예: Partition 0 중심 분배            |
