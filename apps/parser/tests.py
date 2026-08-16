from django.test import TestCase
from apps.parser.parsers import NewsParser

class NewsParserTest(TestCase):
    def test_parse_dates(self):
        parser = NewsParser('https://habr.com/ru/rss/')
        text = 'Сегодня 15.08.2026 состоялась встреча'
        dates = parser.parse_dates(text)
        self.assertEqual(dates, ['15.08.2026'])

    def test_parse_emails(self):
        parser = NewsParser('https://habr.com/ru/rss/')
        text = 'Контакты: test@example.com и admin@site.ru'
        emails = parser.parse_emails(text)
        self.assertEqual(len(emails), 2)
        self.assertIn('test@example.com', emails)
