# Django ORM Watching Storage

Этот проект является частью курса dvmn.org и представляет собой сайт для пульта охранника банка.

## Описание

Проект использует Django ORM для работы с базой данных, позволяя отслеживать сотрудников, которые находятся на объекте, и контролировать их доступ.

## Установка

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Eugene571/django-orm-watching-storage.git
    cd django-orm-watching-storage
    ```

2. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

3. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

## Использование

Перейдите в браузере по адресу `http://127.0.0.1:8000` и используйте интерфейс для управления доступом сотрудников.

## Зависимости

- Django 3.2.*
- Python 3.8 или выше
- Psycopg2 2.9.*
