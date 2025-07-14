### API books library - API для книжной бибилиотеки
### Технологии:
- python 3.12
- django 5.1.3
- djangorestframework 3.15.2
- PostgreSQL
- Celery
- Redis
- Docker, Docker Compose

### Инструкция для развертывания проекта:

#### Клонирование проекта:

git clone https://github.com/


#### Создать виртуальное окружение:
python3 -m venv venv


#### Активировать виртуальное окружение:
source venv/bin/activate

#### Установить зависимости:
pip install -r pyproject.toml


#### Откройте проект в PyCharm, настройте базу данных в settings.py и выполните миграции:
python3 manage.py migrate


#### Для корректной работы проекта, требуется файл .env, который содержит переменные окружения:
Для настройки файла, в корне проекта создайте файл `.env` и заполните его переменными окружения указанными в файле `env.sample`

### Запуск программы
python3 manage.py runserver
