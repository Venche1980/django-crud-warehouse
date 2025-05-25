# Используем базовый образ Python
FROM python:3.10-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Запускаем Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stocks_products.wsgi:application"]
