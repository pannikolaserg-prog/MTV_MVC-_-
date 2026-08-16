FROM python:3.11-slim

WORKDIR /app

# Устанавливаем зависимости
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY src/ .

# Собираем статику
RUN python manage.py collectstatic --noinput --settings=core.settings

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]