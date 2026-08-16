from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from apps.diary.models import DiaryEntry

User = get_user_model()


class DiaryAPIPermissionTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='test123'
        )
        self.user2 = User.objects.create_user(
            username='user2',
            password='test123'
        )

    def test_user_cant_edit_others_entry(self):
        # Получаем токен для user1
        response = self.client.post('/api/token/', {
            'username': 'user1',
            'password': 'test123'
        })
        token1 = response.data['access']

        # Создаем запись от user1
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token1}')
        response = self.client.post('/api/entries/', {
            'title': 'Запись user1',
            'content': 'Тест',
            'is_public': True
        })
        entry_id = response.data['id']

        # Получаем токен для user2
        response = self.client.post('/api/token/', {
            'username': 'user2',
            'password': 'test123'
        })
        token2 = response.data['access']

        # Пытаемся обновить запись user1 от user2
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token2}')
        response = self.client.patch(f'/api/entries/{entry_id}/', {
            'title': 'Изменено user2'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Пытаемся удалить запись user1 от user2
        response = self.client.delete(f'/api/entries/{entry_id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_edit_own_entry(self):
        # Получаем токен для user1
        response = self.client.post('/api/token/', {
            'username': 'user1',
            'password': 'test123'
        })
        token1 = response.data['access']

        # Создаем запись от user1
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token1}')
        response = self.client.post('/api/entries/', {
            'title': 'Моя запись',
            'content': 'Тест',
            'is_public': True
        })
        entry_id = response.data['id']

        # Редактируем свою запись
        response = self.client.patch(f'/api/entries/{entry_id}/', {
            'title': 'Обновлено'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
