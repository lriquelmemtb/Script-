import requests
import urllib3
import json
import conf

urllib3.disable_warnings()

url = "https://192.168.81.253"

#INVENTARIO DISPOSITIVOS CONECTADOS
r = requests.get(url + "/rest/ip/arp", auth=(conf.user, conf.clave), verify=False)
print(json.dumps(r.json(), indent=2))

#VLANadministrador
r1 = requests.put(url + "/interface/vlan", auth=(conf.user, conf.clave), verify=False,
                  data=json.dumps({"name": "Administrador", "vlan-id": "10", "interface": "local"}))
print(json.dumps(r1.json(), indent=2))