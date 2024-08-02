import aiohttp
import asyncio
import os
import json
# import random
from confluent_kafka import Producer
from config import producer_conf

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

producer = Producer(producer_conf)

# ------------------------------------------------------------
# keyword 搜尋(他是從第一頁開始)
# https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keyword}&page={page}&sort=sortParm=rnk&sortOrder=dc
# sort=sortParm=rnk&sortOrder=dc
# 這是有綜合性的排序

# proxies = [
#         "https://107.22.64.25",
#         # "http://proxy2.example.com:8080",
#         # 添加更多代理伺服器
# ]
# proxy = random.choice(proxies)
async def pc_get_keyword_info(keyword, page):
    url = f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keyword}&page={page}&sort=sortParm=rnk&sortOrder=dc"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                response_text = await response.text()
                json_obj = json.loads(response_text)
                print(json_obj)

            else:
                logging.error(f"Error: {response.status}")
                logging.error(await response.text())
                return response.status


# ------------------------------------------------------------
# id 搜尋
# https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{id}&_callback=jsonp_prod
async def pc_get_id_info(item_id):
    url = f"https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{item_id}&_callback=jsonp_prod"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                response_text = await response.text()
                response_text = response_text[15:-48]
                json_obj = json.loads(response_text)
                print(json_obj)

            else:
                logging.error(f"Error: {response.status}")
                logging.error(await response.text())
                return response.status
            
# ------------------------------------------------------------

async def main():
    # await pc_get_id_info("DHAK8A-1900HL6RJ")
    await pc_get_keyword_info('iphone',"1")

if __name__ == "__main__":
    asyncio.run(main())    
            

# # 圖片的前墜：
# https://img.pchome.com.tw/cs/{pic_url}
# ------------------------------------------------------------

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
# def delivery_report(err, msg):
#     if err:
#         print(f'Message delivery failed: {err}')
#     else:
#         print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# def send_to_kafka(topic, data):
#     producer.produce(topic, json.dumps(data).encode('utf-8'), callback=delivery_report)
#     producer.flush()

# async def start_pc_producer():
#     item_id = "DHAK8A-1900HL6RJ" 

#     data = await pc_get_id_info(item_id)
#     if data:
#         send_to_kafka('pc_topic', data)


