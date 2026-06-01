import requests

response = requests.get(
    "http://localhost:8000/predict"
)

print(response.json())
