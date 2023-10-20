import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

url = "https://news.ycombinator.com/news"

url_resp = requests.get(url, verify=False)
url_text = url_resp.text
soup = BeautifulSoup(url_text, "html.parser")
article_tags = soup.find_all("a", {"rel": "noreferrer"})

article_upvote = [int(vote.text.split()[0]) for vote in soup.find_all(name='span', class_='score')]

article_vote_simply_way = []

for vote in soup.find_all(name='span', class_='score'):
    pontuacao = int(vote.text.split()[0])
    article_vote_simply_way.append(pontuacao)

# Initialize variables to keep track of the most voted article
most_voted = 0
most_voted_title = ""
most_voted_link = ""

for i, tag in enumerate(article_tags):
    article_name = tag.getText()
    article_link = tag.get("href")
    upvote = article_upvote[i]

    # Check if the current article has more upvotes than the previous most voted
    if upvote > most_voted:
        most_voted = upvote
        most_voted_title = article_name
        most_voted_link = article_link

print(f"The most voted article is '{most_voted_title}' with {most_voted} upvotes.")
print(f"Link: {most_voted_link}")
