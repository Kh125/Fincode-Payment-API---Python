import requests

api_key = 'YOUR_SECRET_KEY'

order_id = 'ORDER_ID'

url = f'https://api.test.fincode.jp/v1/payments/{order_id}/'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

data = {
    "pay_type": "Card",
    "access_id": "ACCESS_ID", #This id will be provided by settlement registration response like "a_34872347934729347"
    "method": "1",
    "customer_id": "CUSTOMER_ID",
    "card_id": "CARD_ID",
}

try:
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: {response.json()}")
except requests.RequestException as e:
    print(f"Request error: {e}")
