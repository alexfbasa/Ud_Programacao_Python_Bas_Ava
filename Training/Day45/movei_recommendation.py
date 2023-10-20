import requests
import urllib3
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"
urllib3.disable_warnings()
resp = requests.get(url, verify=False)
resp.raise_for_status()
web_site_text = resp.text

soup = BeautifulSoup(web_site_text, "html.parser")

all_titles = soup.find_all("h3", class_="listicleItem_listicle-item__title__hW_Kn")

movie_list = [movie_title.getText() for i, movie_title in enumerate(all_titles)]
movies = movie_list[::-1]

with open("movies_list.txt", "w") as output_list:
    for n in movies:
        output_list.write(f"{n} \n")

# print(movie_list[::-1])
