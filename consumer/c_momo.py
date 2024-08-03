import asyncio
from confluent_kafka import Consumer, KafkaError, KafkaException
import json
from config import consumer_conf
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

consumer = Consumer(consumer_conf)
consumer.subscribe(['momo_topic'])

async def start_momo_consumer(pool):
    try:
        # while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            logging.debug("No message received. Polling again.")
            
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # 正常讀完區塊資料的回報
                logging.info(f"End of partition reached {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                
            else:
                logging.error(f"Error occurred: {msg.error()}")
    
        data = json.loads(msg.value().decode('utf-8'))
        if data:
            async with pool.acquire() as connection:                    
                for n in data:
                    n.get("goodsCode") # 商品賣場id
                    n.get("goodsName") # 商品明
                    n.get("SALE_PRICE") # 商品目前價格
                    n.get("goodsUrl") # 商品連結
                    n.get("goodsFeatureUrl") # 商品詳細資訊
                    n.get("isSpeedArrive") # 能不能速達
                    n.get("imgUrlArray") # 商品圖片list
                    n.get("rating") # 評價
                    n.get("totalSalesInfo").get("text")
                    total_sales_info = n.get("totalSalesInfo")
                    text_value = total_sales_info.get("text") if total_sales_info else None





        # logging.debug(f"consumer_pc 29 {data}")
        # print("consumer_pc 30", data, flush=True)


    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
