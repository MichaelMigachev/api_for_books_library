FROM python:3.11-slim

# Переменные окружения ставим сразу
ENV PYTHONUNBUFFERED=1

# Создаем рабочую директорию
WORKDIR /app

# Устанавливаем только зависимости
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry и требуемые зависимости
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry lock && \
    poetry install --only main --no-root && \
    rm -rf /var/lib/apt/lists/*
                                    # Очищаем список пакетов
# Копируем весь проект
COPY . .

# Команды для запуска: выполнение миграций и запуск сервера
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver"]