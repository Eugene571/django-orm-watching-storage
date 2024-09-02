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
2. Настройка окружения:
Создайте файл .env в корневом каталоге проекта и добавьте в него следующие переменные:
   ``` env
   SECRET_KEY=ваш_секретный_ключ # Секретный ключ, используемый Django для обеспечения безопасности различных криптографических операций
   DEBUG=False # Переключает режим отладки сайта. Имеет логическое значение (True/False). По умолчанию True.
   ALLOWED_HOSTS=* # Список доменов и/или IP-адресов, с которых разрешено обслуживать сайт. По умолчанию не ограничено.
   DB_HOST=адрес_вашей_базы_данных
   DB_NAME=имя_вашей_базы_данных
   DB_USER=пользователь_базы_данных
   DB_PASSWORD=пароль_базы_данных
   DB_PORT=порт_базы_данных
   ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

## Использование

Перейдите в браузере по адресу `http://127.0.0.1:8000` и используйте интерфейс для управления доступом сотрудников.

## Зависимости

- Django 3.2.*
- Python 3.8 или выше
- Psycopg2 2.9.*
- python-dotenv 1.0.1
