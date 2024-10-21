import requests

api_key = 'YOUR_SECRET_KEY'

customer_id = 'CUSTOMER_ID'

url = f'https://api.test.fincode.jp/v1/customers/{customer_id}/cards'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

data = {
    "token": "ENCODED_TOKEN",
    "default_flag": "1",
}

try:
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
    
        print(f"Error: {response.json()}")
except requests.RequestException as e:
    print(f"Request error: {e}")
