# Dockerized Django CRUD Project (Stocks and Products)

This is a Docker image for the Django CRUD project from Netology course.

## Сборка образа

```bash
docker build -t stocks-products .

## Сборка образаЗапуск контейнера
```bash
docker run -d -p 8000:8000 --name stocks-app stocks-products

## Переменные окружения
```bash
Поддерживаемые переменные:

DJANGO_DEBUG=True/False
DJANO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_SECRET_KEY=ваш_секретный_ключ


## Доступные URL
```bash
🔗 http://localhost:8000/admin — админка Django
📦 /api/v1/

## Файлы в репозитории
```bash
В репозиторий должны входить:

Dockerfile — инструкция сборки
.dockerignore — файлы, исключённые из образа
requirements.txt — зависимости Python
manage.py, stocks_products/, logistic/ — структура проекта
