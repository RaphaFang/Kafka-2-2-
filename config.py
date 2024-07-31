# Kafka 配置
producer_conf = {
    'bootstrap.servers': 'kafka:9092',
}

consumer_conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}
