from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/", verify=False)
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')

article_tags = soup.find_all(name='span', class_='titleline')
article_upvote = [int(vote.text.split()[0]) for vote in soup.find_all(name='span', class_='score')]

article_titles = []
article_links = []

for article in article_tags:
    art_text = article.text
    art_link = article.a['href']
    article_titles.append(art_text)
    article_links.append(art_link)

largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(article_titles[largest_index])
print(article_links[largest_index])
