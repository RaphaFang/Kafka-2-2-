import urllib.parse
import requests
import time
import json
import os
from bs4 import BeautifulSoup
import aiohttp
import asyncio

USER_AGENT_VALUE = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

async def momo_get_keyword_info():
    URL = "https://apisearch.momoshop.com.tw/momoSearchCloud/moec/textSearch"
    headers = {'User-Agent': USER_AGENT_VALUE}
    json_data = {
    "host": "momoshop",
    "flag": "searchEngine",
    "data": {
        "specialGoodsType": "",
        "isBrandSeriesPage": False,
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
        "reduceKeyword": "",
        "adSource": "tenmax",
        "addressSearchData": {},
        "rtnCateDatainfo": {
            "cateCode": "",
            "cateLv": "-1",
            "keyword": "iphone 15 pro",
            "curPage": "1",
            "historyDoPush": False,
            "timestamp": 1722570967883
        },
        "searchType": "1",
        "searchValue": "iphone 15 pro",
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
    }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(URL, headers=headers, json=json_data) as response:
            if response.status == 200:
                data = await response.json()
                data = data['rtnSearchData']['goodsInfoList']
                print(data)
                # json_obj = json.loads(response_text)
                # print(json_obj)

    # print(resp)
    # return BeautifulSoup(resp.text, 'html.parser')

# query_str = 'iPhone 7 Plus 128G'
# get_web_content(query_str)
                

                
# "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11859451&Area=search&oid=1_1&cid=index&kw=iphone%2015%20pro"

# https://apisearch.momoshop.com.tw/momoSearchCloud/moec/goodsDetail?i_code=11859451



import aiohttp
from aiohttp import ClientOSError

async def momo_get_id_info():
    URL = "https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=11982320&Area=search&oid=1_1&cid=index&kw=iphone"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL, headers=headers, timeout=aiohttp.ClientTimeout(total=30)) as response:
                if response.status == 200:
                    html_content = await response.text()
                    soup = BeautifulSoup(html_content, 'html.parser')
                    price = soup.find('span', class_='seoPrice')
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



async def main():
    # await momo_get_id_info()
    await momo_get_keyword_info()

if __name__ == "__main__":
    asyncio.run(main())   