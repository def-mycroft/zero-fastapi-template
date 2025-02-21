import requests

url = 'http://localhost:8000/main'
payload = {
    'param1': 'param1',
    'param2': 'param2',
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())


