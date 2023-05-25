import requests


question_data = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get('https://opentdb.com/api.php', params=question_data, verify=False)
response.raise_for_status()
data = response.json()
question_data = data['results']

#
# for i in question_data:
#     print(i['question'])
#     print(i['correct_answer'])
