from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import DiaryEntry

User = get_user_model()


class DiaryTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test123')

    def test_create_entry(self):
        entry = DiaryEntry.objects.create(
            user=self.user,
            title='Test',
            content='Content'
        )
        self.assertEqual(entry.title, 'Test')

    def test_word_count(self):
        entry = DiaryEntry.objects.create(
            user=self.user,
            title='Test',
            content='One two three'
        )
        self.assertEqual(entry.get_word_count(), 3)

    def test_list_view(self):
        self.client.login(username='test', password='test123')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
