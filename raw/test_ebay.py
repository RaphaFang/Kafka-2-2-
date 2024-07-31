# "XfkvLG2fe3AslWGw9gxGwdxpNUXLa01h1rQVbefm20o"
# FangSiYu-pricecom-PRD-4c1eeed77-05b5e5a7
import requests
import os

client_id = os.getenv('EBAY_CLIENT_ID')
client_secret = os.getenv('EBAY_CLIENT_SECRET')

def get_access_token(client_id, client_secret):
    url = "https://api.ebay.com/identity/v1/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "scope": "https://api.ebay.com/oauth/api_scope"
    }
    response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print(f"Error getting token: {response.status_code}")
        return None

access_token = get_access_token(client_id, client_secret)

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
def get_item_info(item_id, access_token):
    url = f"https://api.ebay.com/buy/browse/v1/item/{item_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        item_data = response.json()
        print(item_data)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

item_id = "v1|315072192061|0" 
if item_id:
    get_item_info(item_id, access_token)
