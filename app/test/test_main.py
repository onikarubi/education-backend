import requests

response = requests.get("http://localhost:80")
print(response.json(), response.status_code)
