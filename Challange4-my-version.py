import requests
import json

deviceHttp = 'http://192.168.10.1'


def login():
    import json
    url = deviceHttp + '/api/aaaLogin.json'
    payload = "{\n\t\"aaaUser\": {\n\t\t\"attributes\": {\n    \t\t\"name\" : \"admin\",\n\t\t\t\"pwd\" : \"ciscoapic\"\n\t\t}\n\t}\n}\n"
    headers = {'Content-Type': 'application/json'}

    response = requests.request('POST', url, data=payload, headers=headers)
    json = json.loads(response.text)

    return json['imdata'][0]['aaaLogin']['attributes']['token']


def create_tenant(token, name):
    url = deviceHttp + '/api/node/mo/uni/tn-' + name + '.json'
    payload = "{\r\n\t\"fvTenant\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-" + name + "\",\r\n\t\t\t\"name\": \"acme\",\r\n\t\t\t\"rn\": \"tn-" + name + "\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
    cookie = {'APIC-cookie': token}

    requests.request('POST', url, data=payload, cookies=cookie)


def create_application_profil(token, tenant, name):
    url = deviceHttp + '/api/node/mo/uni/tn-' + tenant + '/ap-' + name + '.json'
    payload = "{\r\n\t\"fvAp\": {\r\n\t\t\"attributes\": {\r\n\t\t\t\"dn\": \"uni/tn-"+tenant+"/ap-"+name+"\",\r\n\t\t\t\"name\": \""+name+"\",\r\n\t\t\t\"rn\": \"ap-"+name+"\",\r\n\t\t\t\"status\": \"created\"\r\n\t\t},\r\n\t\t\"children\": []\r\n\t}\r\n}"
    cookie = {'APIC-cookie': token}

    requests.request('POST', url, data=payload, cookies=cookie)


def create_epg(token, tenant, profil, name):
    url = deviceHttp + '/api/node/mo/uni/tn-'+tenant+'/ap-'+profil+'/epg-'+name+'.json'
    payload = "{\"fvAEPg\":{\"attributes\":{\"dn\":\"uni/tn-"+tenant+"/ap-"+profil+"/epg-"+name+"\",\"name\":\""+name+"\",\"rn\":\"epg-"+name+"\",\"status\":\"created\"},\"children\":[{\"fvCrtrn\":{\"attributes\":{\"dn\":\"uni/tn-"+tenant+"/ap-"+profil+"/epg-"+name+"/crtrn\",\"name\":\"default\",\"rn\":\"crtrn\",\"status\":\"created,modified\"},\"children\":[]}}]}}\r\nresponse: {\"totalCount\":\"0\",\"imdata\":[]}"
    cookie = {'APIC-cookie': token}

    requests.request('POST', url, data=payload, cookies=cookie)


if __name__ == "__main__":
    login_token = (login())
    create_tenant(login_token, 'acme')
    create_application_profil(login_token, 'acme', 'Accounting')
    create_epg(login(), 'acme', 'Accounting', 'Bills')
    create_epg(login(), 'acme', 'Accounting', 'Payroll')
