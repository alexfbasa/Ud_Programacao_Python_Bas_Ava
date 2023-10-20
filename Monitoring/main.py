import requests
import urllib3
from bs4 import BeautifulSoup

# Disable SSL certificate verification warnings
urllib3.disable_warnings()

home_page = "https://home.kuehne-nagel.com/"

resp = requests.get(home_page, verify=True)
resp.raise_for_status()

html = resp.text
soup = BeautifulSoup(html, "html.parser")

all_anchor_tag = soup.find_all("link", {"data-senna-track": "temporary", "rel": "alternate"})

links = []

with open("links.txt", "w") as output_file:
    for tag in all_anchor_tag:
        href = tag.get("href")
        output_file.write(href + "\n")

with open("links.txt", "r") as input_file:
    links = input_file.readlines()

for link in links:
    link = link.strip()
    try:
        url_response = requests.get(link, verify=False)
        if url_response.status_code == 200:
            print(f"URL {link} is working fine.")
        else:
            print(f"URL {link} returned status code {url_response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Error while trying to access URL {link}: {e}")
