## API books library - API для книжной бибилиотеки
### 🛠 Технологии
- **Python** 3.11+
- **Django** 5.2
- **Django REST Framework** (DRF) 3.15
- **PostgreSQL** — база данных
- **Celery** + **Redis** — фоновые задачи и брокер сообщений
- **Docker** + **Docker Compose** — контейнеризация
- **drf-spectacular** — автоматическая документация API (Swagger / ReDoc)

### Инструкция для развертывания проекта:

#### Клонирование проекта:

git clone https://github.com/MichaelMigachev/api_for_books_library/tree/develop


#### Создать виртуальное окружение:
python3 -m venv venv


#### Активировать виртуальное окружение:
source venv/bin/activate

#### Установить зависимости:
pip install -r pyproject.toml


#### Откройте проект в PyCharm, настройте базу данных в settings.py и выполните миграции:
python manage.py migrate


#### Для корректной работы проекта, требуется файл .env, который содержит переменные окружения:
Для настройки файла, в корне проекта создайте файл `.env` и заполните его переменными окружения указанными в файле `env.sample`

### Запуск программы
python manage.py runserver

### Запуск фоновых задач (рассылка напоминаний)
#### Запустить Redis в отдельном терминале выполните:
redis-server.exe
#### в терминале запустите celery worker командой
celery -A config worker -l INFO
#### Команда для windows:
##### Перед этим убедитесь, что eventlet установлен: pip install eventlet
celery -A config worker -l INFO -P eventlet

### Документация будет доступна по адресам:

Swagger
http://localhost:8000/swagger/

ReDoc 
http://localhost:8000/redoc/

JSON-схема  
http://localhost:8000/schema/

### Запуск через Docker Compose:
#### Перед запуском обновите .env: 
POSTGRES_HOST=db
CELERY_BROKER_URL=redis://redis:6379/1
CELERY_RESULT_BACKEND=redis://redis:6379/1

#### Для запуска всех сервисов выполните команду:
docker-compose up --build

#### Для запуска в фоновом режиме:
docker-compose up -d

#### После запуска доступность сервисов можно проверить командой:
docker-compose ps



### Автор проекта Михаил Мигачев