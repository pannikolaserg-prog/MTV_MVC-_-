from django.test import TestCase
from django.conf import settings
from apps.utils.email import send_email_notification
from apps.diary.models import DiaryEntry
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailUtilsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='test123'
        )
        self.entry = DiaryEntry.objects.create(
            user=self.user,
            title='Тест',
            content='Содержание'
        )

    def test_send_email_notification(self):
        result = send_email_notification(self.user, self.entry)
        self.assertTrue(result)
