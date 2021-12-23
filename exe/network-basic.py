import requests

response = requests.get("https://randomuser.me/api/?results=7")
data = response.json()

for user in data["results"]:
    print(user["name"]["first"])

response = requests.get("https://httpbin.org/ip")
print(response.json())
