import requests
import urllib3
import json
import conf

urllib3.disable_warnings()
url = "https://192.168.81.253"

r = requests.get(url + "/rest/ip/address/*3", auth=(conf.user, conf.clave), verify=False)
print(json.dumps(r.json(), indent=2))
