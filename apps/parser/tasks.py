from celery import shared_task
from .parsers import NewsParser

@shared_task
def parse_news_task(url):
    parser = NewsParser(url)
    news = parser.parse_news()
    return {'news': news, 'count': len(news)}
