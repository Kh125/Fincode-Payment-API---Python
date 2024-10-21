import requests

api_key = 'SECRET_KEY'

url = f'https://api.test.fincode.jp/v1/customers'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

data = {
    "name": "Mary",
    "email": "mary@example.com"
}

try:
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print(f"Success: {response.json()}")
    else:
        print(f"Error: {response.json()}")
except requests.RequestException as e:

    print(f"Request error: {e}")
