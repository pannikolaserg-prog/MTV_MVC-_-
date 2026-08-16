import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.diary.models import DiaryEntry

User = get_user_model()

class DiaryEntryModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='test123'
        )
        self.entry = DiaryEntry.objects.create(
            user=self.user,
            title='Тестовая запись',
            content='Тестовое содержание',
            tags=['тест', 'важно']
        )

    def test_entry_creation(self):
        self.assertEqual(self.entry.title, 'Тестовая запись')
        self.assertEqual(self.entry.user.username, 'testuser')

    def test_entry_str(self):
        self.assertEqual(str(self.entry), 'Тестовая запись')

    def test_tags_field(self):
        self.assertIn('тест', self.entry.tags)
        self.assertIn('важно', self.entry.tags)


class DiaryEntryViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='test123'
        )
        self.client.login(username='testuser', password='test123')

    def test_entry_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_entry_detail_view(self):
        entry = DiaryEntry.objects.create(
            user=self.user,
            title='Детальная запись',
            content='Содержание'
        )
        response = self.client.get(f'/{entry.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Детальная запись')

    def test_entry_delete_view(self):
        entry = DiaryEntry.objects.create(
            user=self.user,
            title='Запись для удаления',
            content='Содержание'
        )
        self.assertEqual(DiaryEntry.objects.count(), 1)
        response = self.client.post(f'/{entry.id}/delete/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(DiaryEntry.objects.count(), 0)

    def test_export_json(self):
        DiaryEntry.objects.create(
            user=self.user,
            title='Экспорт JSON',
            content='Тест'
        )
        response = self.client.get('/export/json/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_export_csv(self):
        DiaryEntry.objects.create(
            user=self.user,
            title='Экспорт CSV',
            content='Тест'
        )
        response = self.client.get('/export/csv/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'text/csv; charset=utf-8')

    def test_search_entries(self):
        """Тест поиска записей"""
        DiaryEntry.objects.create(
            user=self.user,
            title='Важная запись',
            content='Содержание для поиска'
        )
        response = self.client.get('/?search=Важная')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Важная запись')

    def test_filter_public_entries(self):
        """Тест фильтрации публичных записей"""
        DiaryEntry.objects.create(
            user=self.user,
            title='Публичная запись',
            content='Тест',
            is_public=True
        )
        DiaryEntry.objects.create(
            user=self.user,
            title='Приватная запись',
            content='Тест',
            is_public=False
        )
        response = self.client.get('/?is_public=true')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Публичная запись')
        self.assertNotContains(response, 'Приватная запись')

    def test_404_page(self):
        """Тест страницы 404"""
        response = self.client.get('/99999/')
        self.assertEqual(response.status_code, 404)

    def test_redirect_after_login(self):
        """Тест редиректа после входа"""
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Редирект на логин
        self.assertRedirects(response, '/users/login/?next=/')
