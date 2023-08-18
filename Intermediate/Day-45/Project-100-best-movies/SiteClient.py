import json

import requests
from bs4 import BeautifulSoup


class SiteClient:

    def __init__(self):
        self.empire_host = "https://www.empireonline.com/movies/features/best-movies-2/"

    def get(self):
        resp = requests.get(f"{self.empire_host}", verify=False)
        empire_web_page = resp.text
        return empire_web_page

    def find_movies(self):
        soup = BeautifulSoup(self.get(), 'html.parser')
        movies = []
        movie_divs = soup.find_all('div', class_='jsx-4245974604')
        for div in movie_divs:
            # Extract movie title and other relevant information
            title = div.find('a').question_text
            review_link = div.find('a')['href']
            review_text = div.find('p').find('a').question_text

            # Create a dictionary with the movie information
            movie = {
                'title': title,
                'review_link': review_link,
                'review_text': review_text
            }

            # Add the movie to the list
            return movies.append(movie)
