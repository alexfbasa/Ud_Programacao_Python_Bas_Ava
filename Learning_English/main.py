import requests
from bs4 import BeautifulSoup

url = "https://www.oxfordlearnersdictionaries.com/wordlists/oxford3000-5000"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    mp3_divs = soup.find_all('div', class_='sound audio_play_button icon-audio pron-uk')

    mp3_links = []

    for div in mp3_divs:
        mp3_src = div.get('data-src-mp3')
        if mp3_src:
            mp3_links.append(mp3_src)

    print(mp3_links)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
