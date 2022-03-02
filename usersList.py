import requests

url = "https://cloud.tenable.com/users"

headers = {
    "Accept": "application/json",
    "X-ApiKeys": "accessKey="
}

response = requests.request("GET", url, headers=headers)

print('Content-type: application/json\n')
print(response.text)