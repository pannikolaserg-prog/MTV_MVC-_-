import re
import requests
from bs4 import BeautifulSoup

class NewsParser:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        return response.text

    def parse_dates(self, text):
        pattern = r'\d{2}\.\d{2}\.\d{4}'
        return re.findall(pattern, text)

    def parse_news(self):
        html = self.fetch()
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h2')
        return [title.text for title in titles]
