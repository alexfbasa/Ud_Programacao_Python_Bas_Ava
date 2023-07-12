from bs4 import BeautifulSoup
from SiteClient import SiteClient


class SiteCodeGenerator:

    def __init__(self):
        self.client = SiteClient()
        self.package_dir = "/generated"

    def generate(self):
        self.generate_WebPageData_py()

    def generate_WebPageData_py(self):
        file_path = f"{self.package_dir}/index.html"
        web_site_data = self.client.find_movies()
        with open(file_path, 'w') as f:
            f.write("<!DOCTYPE html>")
            f.write(f"<html lang='en'>")
            f.write(f"    <meta charset='UTF-8'>")
            for movie in web_site_data:
                pass
