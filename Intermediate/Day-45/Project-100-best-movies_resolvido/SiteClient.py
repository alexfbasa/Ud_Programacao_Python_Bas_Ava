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
        return soup

    def show_pretty(self):
        resp = self.find_movies().prettify()
        return resp

    def find_movie_titles(self):
        soup = self.find_movies()
        script_tags = soup.find_all('script')
        return script_tags




