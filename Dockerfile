FROM python:3.11-slim

# Устанавливаем необходимые системные зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем только файл с зависимостями
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry (более надежный способ)
RUN pip install --upgrade pip && \
    pip install poetry==1.7.0

# Устанавливаем зависимости проекта
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root --no-interaction

# Копируем остальные файлы проекта
COPY . .

# Устанавливаем переменную окружения
ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]