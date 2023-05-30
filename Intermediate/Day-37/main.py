import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_TOKEN = "uya82hauhyeauhsd2"
PIXELA_USERNAME = "alexbasa"
graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"
graph_id = "graph1"
pixel_creation_endpoint = f"{graph_endpoint}/{graph_id}"

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_config = {
    'id': graph_id,
    'name': "Days-of-Coding",
    'unit': "Days",
    'type': "int",
    'color': "ajisai",
}
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

currently_date = datetime.now()
formatted_day = currently_date.strftime("%Y%m%d")

pixel_data = {
    'date': formatted_day,
    'quantity': '1',
}
updated_endpoint = f"{pixel_creation_endpoint}/{formatted_day}"
# Create a user
# response = requests.post(url=pixela_endpoint, json=user_params, verify=False)
# Create a new Graph
# create_graph = requests.post(url=graph_endpoint, json=graph_config, headers=headers, verify=False)
# print(create_graph.text)
# Check the new graph
# https://pixe.la/v1/users/alexbasa/graphs/graph1.html

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers, verify=False)
# print(response.text)