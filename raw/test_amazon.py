import requests
import os

# url = "https://real-time-amazon-data.p.rapidapi.com/search"
# querystring = {"query":"Phone","page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL"}
# headers = {
# 	"x-rapidapi-key": "69462e7a65mshc0fa7a733f61498p156f01jsn6ca7f0a1167b",
# 	"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())


# # ------------------------------------------------------------
# id 查詢
# 他有提供商品描述
# url = "https://real-time-amazon-data.p.rapidapi.com/product-details"
# querystring = {"asin":"B09SM24S8C","country":"US"}
# headers = {
# 	"x-rapidapi-key": os.getenv('X_rapidapi_key'),
# 	"x-rapidapi-host": os.getenv('X_rapidapi_host')
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())

# # # # ------------------------------------------------------------
# # Product Offers
# # 這之api可以推送相同asin的不同賣家
# import requests

# url = "https://real-time-amazon-data.p.rapidapi.com/product-offers"
# querystring = {"asin":"B09SM24S8C","country":"US","limit":"100","page":"1"}
# headers = {
# 	"x-rapidapi-key": os.getenv('X_rapidapi_key'),
# 	"x-rapidapi-host": os.getenv('X_rapidapi_host')
# }

# response = requests.get(url, headers=headers, params=querystring)

# print(response.json())