import re
import requests
from bs4 import BeautifulSoup


class NewsParser:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'  # Добавляем для правильной кодировки
        return response.text

    def parse_dates(self, text):
        pattern = r'\d{2}\.\d{2}\.\d{4}'
        return re.findall(pattern, text)

    def parse_news(self):
        html = self.fetch()
        soup = BeautifulSoup(html, 'xml')

        # Ищем все элементы item в RSS
        items = soup.find_all('item')
        news = []

        for item in items:
            # Извлекаем заголовок
            title = item.find('title')
            title_text = title.text if title else 'Без заголовка'

            # Извлекаем ссылку
            link = item.find('link')
            link_text = link.text if link else ''

            # Извлекаем описание
            description = item.find('description')
            description_text = description.text if description else ''

            # Извлекаем дату публикации
            pub_date = item.find('pubDate')
            pub_date_text = pub_date.text if pub_date else ''

            news.append({
                'title': title_text,
                'link': link_text,
                'description': description_text,
                'pubDate': pub_date_text
            })

        return news
