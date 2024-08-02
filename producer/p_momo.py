import aiohttp
import asyncio
import os
import json
from bs4 import BeautifulSoup
from confluent_kafka import Producer
from config import producer_conf

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

producer = Producer(producer_conf)

# ------------------------------------------------------------
# proxies = [
#         "https://107.22.64.25",
#         # "http://proxy2.example.com:8080",
#         # 添加更多代理伺服器
# ]
# proxy = random.choice(proxies)
USER_AGENT_VALUE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
async def momo_get_keyword_info(keyword):
    URL = "https://apisearch.momoshop.com.tw/momoSearchCloud/moec/textSearch"
    headers = {'User-Agent': USER_AGENT_VALUE}
    json_data = {
    "host": "momoshop",
    "flag": "searchEngine",
    "data": {
        "specialGoodsType": "",
        "isBrandSeriesPage": False,
        "reduceKeyword": "",
        "adSource": "tenmax",
        "addressSearchData": {},
        "rtnCateDatainfo": {
            "cateCode": "",
            "cateLv": "-1",
            "keyword": keyword,
            "curPage": "1",
            "historyDoPush": False,
            "timestamp": 1722570967883
        },
        "searchType": "1",
        "searchValue": keyword,
        # "authorNo": "",
        # "originalCateCode": "",
        # "cateCode": "",
        # "cateLevel": "-1",
        # "cateType": "",
        # "china": "N",
        # "cod": "N",
        # "cp": "N",
        # "curPage": "1",
        # "cycle": "N",
        # "first": "N",
        # "flag": 2018,
        # "freeze": "N",
        # "isBrandSeriesPage": False,
        # "originalCateCode": "",
        # "prefere": "N",
        # "priceE": "99999999",
        # "priceS": "0",
        # "serviceCode": "MT01",
        # "showType": "chessboardType",
        # "specialGoodsType": "",
        # "stockYN": "N",
        # "superstore": "N",
        # "superstorePay": "N",
        # "threeHours": "N",
        # "tomorrow": "N",
        # "tvshop": "N",
        # "video": "N"
        }}

    async with aiohttp.ClientSession() as session:
        async with session.post(URL, headers=headers, json=json_data) as response:
            if response.status == 200:
                data = await response.json()
                
                data = data['rtnSearchData']['goodsInfoList']  # 這邊會有30筆
                await asyncio.sleep(2)

                return data
# ------------------------------------------------------------
# id 搜尋
import aiohttp
from aiohttp import ClientOSError

async def momo_get_id_info(item_id):
    URL = f"https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code={item_id}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL, headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as response:
                if response.status == 200:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    price = soup.find('span', class_='seoPrice')
                    await asyncio.sleep(2)
                    if price:
                        print(price.text.strip())
                    else:
                        print("未找到价格信息")
                else:
                    print(f"请求失败，状态码：{response.status}")
    except ClientOSError as e:
        print(f"连接错误：{e}")
    except Exception as e:
        print(f"其他错误：{e}")
            
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
def delivery_report(err, msg):
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def send_to_kafka(topic, data):
    producer.produce(topic, json.dumps(data).encode('utf-8'), callback=delivery_report)
    producer.flush()

async def start_pc_producer(keyword):
    item_id = "11982320"
    keyword = '放入搜尋字串'

    data = await momo_get_keyword_info(keyword)
    # price = await momo_get_id_info(item_id)
    if data:
        send_to_kafka('momo_topic', data)


