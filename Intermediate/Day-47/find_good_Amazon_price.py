import requests
import urllib3
from bs4 import BeautifulSoup

url = "https://www.amazon.com/GeeekPi-Raspberry-8GB-Starter-Kit/dp/B09LYP7QH3/ref=sr_1_4?keywords=raspberry+pi&qid=1698047001&s=books&sr=1-4-catcorr"

urllib3.disable_warnings()

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "es-CO,es-419;q=0.9,es;q=0.8,en;q=0.7",
    'referer': 'https://www.amazon.com/'
}

resp = requests.get(url, verify=False, headers=header)

url_text = resp.content

soup = BeautifulSoup(url_text, "lxml")

print(soup.prettify())
