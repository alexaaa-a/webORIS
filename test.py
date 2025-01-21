import requests

url = 'http://localhost:8000'
data = {'key': 'value'}
response = requests.post(url, data=data)

print(response.text)