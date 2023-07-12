
from SiteClient import SiteClient


site_client = SiteClient()
titles = site_client.find_movie_titles()
print(titles)

