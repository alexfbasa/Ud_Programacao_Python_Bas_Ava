import requests

url = "https://opentdb.com/api.php"
parameters = {
    "amount": 10,
    "type": "boolean"
}

res = requests.get(url, verify=False, params=parameters)
res.raise_for_status()
res_json = res.json()
question_data = res_json['results']

