import requests

api_key = 'YOUR_SECRET_KEY'

url = f'https://api.test.fincode.jp/v1/payments'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

customer_id = "CUSTOMER_ID",
card_id = "CARD_ID"

data = {
    "pay_type": "Card",
    "job_code": "CAPTURE",
    "customer_id": customer_id,
    "card_id": card_id,
    "amount": "2300"
}

try:
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: {response.json()}")
except requests.RequestException as e:
    print(f"Request error: {e}")
