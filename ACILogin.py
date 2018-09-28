import requests

url = "http://192.168.10.1/api/aaaLogin.json"

payload = "{\n\"aaaUser\": {\n\t\"attributes\":{\n\t\t\"name\":\"admin\",\n\t\t\"pwd\": \"ciscoapic\"\n\t}\n}\n}"
headers = {'Content-Type': 'application/json'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
