import requests

url = "http://192.168.10.80/restconf/api/config/native/interface/Loopback/500"

payload = "{\n\t\"ned:Loopback\": {\n\t\t\"name\": 500,\n\t\t\"ip\": {\n\t\t\t\"address\":{\n\t\t\t\t\"primary\":{\n\t\t\t\t\t\"address\": \"170.99.1.1\",\n\t\t\t\t\t\"mask\": \"255.255.255.0\"\n\t\t\t\t}\n\t\t\t}\n\t\t\t\n\t\t}\n\t}\n}"
headers = {
    'Content-Type': "application/vnd.yang.data+json",
    'Accept': "application/vnd.yang.data+json",
    'Authorization': "Basic YWRtaW46Y2lzY28="
    }

response = requests.request("PUT", url, data=payload, headers=headers)

print(response.text)