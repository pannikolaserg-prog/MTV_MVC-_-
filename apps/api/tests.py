from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from apps.diary.models import DiaryEntry

User = get_user_model()

class DiaryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='test123'
        )
        # Получаем токен
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'test123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get_entries(self):
        """Тест получения списка записей через API"""
        response = self.client.get('/api/entries/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_entry_api(self):
        """Тест создания записи через API"""
        response = self.client.post('/api/entries/', {
            'title': 'API запись',
            'content': 'Создано через API',
            'is_public': True
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DiaryEntry.objects.count(), 1)
        self.assertEqual(DiaryEntry.objects.first().title, 'API запись')

    def test_create_entry_without_auth(self):
        """Тест создания записи без авторизации (должна быть ошибка)"""
        self.client.credentials()  # Убираем токен
        response = self.client.post('/api/entries/', {
            'title': 'Неавторизованная запись',
            'content': 'Должна быть ошибка'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

