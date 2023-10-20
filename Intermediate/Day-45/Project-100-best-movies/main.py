import json
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/", verify=False)
movies_webpage = response.text
soup = BeautifulSoup(movies_webpage, "html.parser")
# data = json.loads(soup.select_one("__NEXT_DATA__").contents[0])
# data = soup.select_one("disclaimer_disclaimer__ZAJ2A")
# data_dict = data["props"]["pageProps"]["apolloState"]

# print(data)

# movie_list = []
# for key, value in data_dict.items():
#     if key.startswith("ImageMeta"):
#         movie = {
#             "title": value.get("titleText"),
#             "description": value.get("description"),
#             "image_url": value["image"].get("path"),
#             "amazon_link": value.get("amazonId")
#         }
#         movie_list.append(movie)
#
# # Print the movie list
# for movie in movie_list:
#     print("Title:", movie["title"])
#     print("Description:", movie["description"])
#     print("Image URL:", movie["image_url"])
#     print("Amazon Link:", movie["amazon_link"])
#     print("----------------------------------")
