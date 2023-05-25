import requests

question_data = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php', params=question_data, verify=False)
response.raise_for_status()
data = response.json()
# question_data = data['results']
print(data['results'][0]['question'])

print(question_data)
