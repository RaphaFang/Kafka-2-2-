import requests
import urllib
import json


keyword = '手機保護殼'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68',
    'x-api-source': 'pc',
    'referer': f'https://shopee.tw/search?keyword={urllib.parse.quote(keyword)}'
}

s = requests.Session()
url = 'https://shopee.tw/api/v4/search/product_labels'
r = s.get(url, headers=headers)

base_url = 'https://shopee.tw/api/v2/search_items/'
query = f"by=relevancy&keyword={keyword}&limit=50&newest=0&order=desc&page_type=search&version=2"
url = base_url + '?' + query
r = s.get(url, headers=headers)
print(r.status_code)
print(r.json)
if r.status_code == requests.codes.ok:
    data = r.json()
    print(data)