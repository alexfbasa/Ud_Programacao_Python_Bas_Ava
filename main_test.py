import requests

url = "https://elasticsearch-cp-444640.apps.emea.ocp.int.kn/_cat/nodes?&v=true&h=" \
      "ip,name,disk.avail,disk.used,disk.total&format=json"

response = requests.get(url)
data_item = response.json()

for data in data_item:
    print(data['disk.avail'])
