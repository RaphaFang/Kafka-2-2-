# "XfkvLG2fe3AslWGw9gxGwdxpNUXLa01h1rQVbefm20o"
# FangSiYu-pricecom-PRD-4c1eeed77-05b5e5a7
# import requests
import aiohttp
import os
import requests
import json
from confluent_kafka import Producer
from config import producer_conf

producer = Producer(producer_conf)

# ------------------------------------------------------------
client_id = os.getenv('EBAY_CLIENT_ID')
client_secret = os.getenv('EBAY_CLIENT_SECRET')
    
async def get_access_token(client_id, client_secret):
    url = "https://api.ebay.com/identity/v1/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    async with aiohttp.ClientSession() as session:
        auth = aiohttp.BasicAuth(client_id, client_secret)
        async with session.post(url, headers=headers, data=data, auth=auth) as response:
            if response.status == 200:
                token_response = await response.json()
                return token_response["access_token"]
                # 總之不能寫在一起，return await response.json() 會報錯
            else:
                print(f"get_access_token ->,Error: {response.status}")
                return None

# ------------------------------------------------------------
# def search_items_by_keyword(keyword, access_token):
#     url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
#     params = {
#         "q": keyword,
#         "limit": 5
#     }
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     response = requests.get(url, headers=headers, params=params)
    
#     if response.status_code == 200:
#         search_results = response.json()
#         if "itemSummaries" in search_results:
#             item_id = search_results["itemSummaries"][0]["itemId"]
#             print(f"Found item ID: {item_id}")
#             return item_id
#         else:
#             print("No items found")
#             return None
#     else:
#         print(f"Error: {response.status_code}")
#         print(response.text)
#         return None

# keyword = "laptop" 
# item_id = search_items_by_keyword(keyword, access_token)

# ------------------------------------------------------------
async def ebay_get_id_info(item_id, access_token):
    if access_token:
        url = f"https://api.ebay.com/buy/browse/v1/item/{item_id}"
        headers = {
            "Authorization": f"Bearer {access_token}"
        }
        # !
        # async def fetch_data(session, url):
        #     async with session.get(url) as response:
        #         return await response.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    item_data = await response.json()
                    return item_data
                else:
                    print(f"Error: {response.status}")
                    print(await response.text())
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

async def start_ebay_producer():
    item_id = "v1|315072192061|0" 
    access_token = await get_access_token(client_id, client_secret)
    # 這邊的access_token，應該不需要每一次任務都打，我記得他的有效期限是兩小時，或許可以看情況打
    if access_token:
        data = await ebay_get_id_info(item_id, access_token)
        if data:
            send_to_kafka('ebay_topic', data)



# ! 流程
# DB得到全部的item url，存放到 api_urls
# 把api_urls的資料味進去 ebay_get_id_info()
# ebay_get_id_info()的資料，最後送到 start_producer()