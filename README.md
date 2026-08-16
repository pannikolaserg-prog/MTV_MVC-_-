# 📝 Веб-приложение для ведения личного дневника

## Описание
Веб-приложение для ведения личного дневника с возможностью создания, редактирования и управления записями.

## Стек технологий
- **Backend**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL
- **Auth**: JWT (JSON Web Token)
- **Container**: Docker, Docker Compose
- **Documentation**: Swagger/OpenAPI
- **Other**: Celery, Redis, Telegram Bot API

## Установка и запуск

### Локально
```bash
cd src
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
