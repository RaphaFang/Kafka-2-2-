# source: https://clu.gitbook.io/python-web-crawler-note/72-pchome-24h-apipa-chong

import requests
from requests.adapters import HTTPAdapter

def get_item_info(item_id, ):
    url = f"https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E9%8D%B5%E7%9B%A4&page=2&sort=sale/dc"
    url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page={}&sort=sale/dc"

    response = requests.get(url)
    
    if response.status_code == 200:
        item_data = response.json()
        print(item_data)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

item_id = "v1|315072192061|0" 
if item_id:
    get_item_info(item_id)


# keyword 搜尋
# https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keyword}&page={page}&sort=sortParm=rnk&sortOrder=dc
# sort=sortParm=rnk&sortOrder=dc
# 這是有綜合性的排序
    
# id 搜尋
# https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/{id}&_callback=jsonp_prod
    # 要切一下回來的資料

# 更詳細
# Price: 價格信息，包括市場價（M），促銷價（P），最低價（Low）
# https://ecapi-pchome.cdn.hinet.net/cdn/ecshop/prodapi/v2/prod/DSAAFR-A900GD4JC/desc&_callback=jsonp_prod
# https://ecapi.pchome.com.tw/ecshop/prodapi/v2/prod/DHAFI0-A900BAPXK/desc&_callback=jsonp_prod

# 圖片的前墜：
# https://img.pchome.com.tw/cs/{pic_url}
