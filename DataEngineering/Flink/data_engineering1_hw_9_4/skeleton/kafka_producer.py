from kafka import KafkaProducer
import json
import time
import random

# Kafka 브로커 주소는 'localhost:9092'입니다.
# 메시지는 JSON 형식으로 직렬화되어 전송되어야 합니다.
# → value_serializer를 설정할 것
# 전송할 데이터는 다음과 같은 딕셔너리입니다
'''
{
    "sensor_id": "sensor-1",
    "location": "lab",
    "temperature": 25.3,
    "humidity": 50.1,
    "status": "OK"
}
'''

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sensor_ids = ['sensor-1', 'sensor-2']
locations = ['lab', 'office']

# 1초에 하나씩 데이터를 전송합니다.
for _ in range(100):
    data = {
        'sensor_id': random.choice(sensor_ids),
        'location': random.choice(locations),
        'temperature': round(random.uniform(20, 30), 2),
        'humidity': round(random.uniform(40, 60), 2),
        'status': random.choice(['OK', 'WARN', 'FAIL'])
    }
    producer.send('sensor_readings', value=data)
    print("[SEND]", data)
    time.sleep(1)
 