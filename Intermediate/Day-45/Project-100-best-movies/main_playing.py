import json
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/", verify=False)
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, "html.parser")

movie_name_element = soup.find_all(name='h3', class_='jsx-4245974604')

movie_names = []

for element in movie_name_element:
    movie_name = element.text.strip()
    movie_names.append(movie_name)

for name in movie_names:
    print(name)
