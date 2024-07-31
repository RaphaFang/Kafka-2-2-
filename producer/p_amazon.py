import aiohttp
import os
import json
from confluent_kafka import Producer
from config import producer_conf

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

producer = Producer(producer_conf)

# ------------------------------------------------------------
async def amazon_get_id_info(item_id):
    url = "https://real-time-amazon-data.p.rapidapi.com/product-details"
    querystring = {"asin":item_id,"country":"US"}
    headers = {
	    "x-rapidapi-key": os.getenv('X_rapidapi_key'),
	    "x-rapidapi-host": os.getenv('X_rapidapi_host')
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=querystring) as response:
            if response.status == 200:
                item_data = await response.json()
                logging.info(item_data)                
                return item_data
            else:
                logging.error(f"Error: {response.status}")
                logging.error(await response.text())
                return response.status
                
        # !這邊是真正多比資料的蒐集
        # api_urls = [
        #     'https://api.example.com/data1',
        #     'https://api.example.com/data2',
        #     # 添加更多的 API URL
        # ]

        # async with aiohttp.ClientSession() as session:
        #     tasks = [fetch_data(session, url) for url in api_urls]
        #     responses = await asyncio.gather(*tasks)

        #     for data in responses:
        #         send_to_kafka('my_topic', data)

# ------------------------------------------------------------
def delivery_report(err, msg):
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_to_kafka(topic, data):
    producer.produce(topic, json.dumps(data).encode('utf-8'), callback=delivery_report)
    producer.flush()

async def start_amazon_producer():
    item_id = "B09SM24S8C" 

    data = await amazon_get_id_info(item_id)
    if data:
        send_to_kafka('amazon_topic', data)



# ! 流程
# DB得到全部的item url，存放到 api_urls
# 把api_urls的資料味進去 ebay_get_id_info()
# ebay_get_id_info()的資料，最後送到 start_producer()