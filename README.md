# Foodgram - Продуктовый помощник

## Описание проекта

Foodgram - это веб-приложение, которое позволяет пользователям публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в избранное, скачивать список продуктов, необходимых для приготовления блюд.

## Стек технологий
- Python 3.9
- Django REST framework
- PostgreSQL
- Docker
- nginx
- gunicorn
- GitHub Actions

## Ссылки на сайт и документацию

## Инструкция по запуску проекта

### Локальный запуск проекта

1. Клонируйте репозиторий:

```bash
git clone git@github.com:ElizavetaPerevalova/foodgram.git
```

2. Создайте файл .env в корневой директории со следующим содержимым:

```bash
cd foodgram
# Django settings
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
DB
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

3. Запустите docker-compose:

```bash
sudo docker compose up --build -d
```

4. Выполните миграции:

```bash
sudo docker compose exec backend python manage.py migrate
```

5. Соберите статику:

```bash
sudo docker compose exec backend python manage.py collectstatic --no-input
``` 

6. Создайте суперпользователя:

```bash
sudo docker compose exec backend python manage.py createsuperuser
```


### Запуск проекта на сервере

1. Установите docker и docker-compose на сервер

2. Скопируйте файлы docker-compose.production.yml и .env на сервер

3. Запустите контейнеры:

```bash
sudo docker compose -f docker-compose.production.yml up -d
```

4. Выполните миграции:

```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
```

5. Соберите статику:

```bash
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic --no-input
```


## CI/CD

Для проекта настроен Continuous Integration и Continuous Deployment:

- Автоматический запуск тестов
- Обновление образов на Docker Hub
- Автоматический деплой на боевой сервер
- Отправка уведомления в Telegram о успешном деплое

## Документация API

Документация доступна по эндпоинту: http://51.250.27.110/api/docs/

## Доступ к проекту

Проект доступен по адресу: http://51.250.27.110/, http://lisafoodgram.zapto.org/
API проекта: http://51.250.27.110/api/

## Основные эндпоинты API

- ```/api/users/``` - пользователи
- ```/api/tags/``` - теги
- ```/api/ingredients/``` - ингредиенты
- ```/api/recipes/``` - рецепты

## Примеры запросов API  
http://127.0.0.1:8000/api/ingredients/4/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 4,
    "name": "мясо",
    "measurement_unit": "г"
}
{"id":4,"name":"мясо","measurement_unit":"г"}

http://127.0.0.1:8000/api/ingredients/
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 3,
        "name": "Кузя",
        "measurement_unit": "по вкусу"
    },
    {
        "id": 2,
        "name": "молоко",
        "measurement_unit": "мл"
    },
    {
        "id": 4,
        "name": "мясо",
        "measurement_unit": "г"
    },
    {
        "id": 1,
        "name": "яйцо",
        "measurement_unit": "шт"
    }
]
[{"id":3,"name":"Кузя","measurement_unit":"по вкусу"},{"id":2,"name":"молоко","measurement_unit":"мл"},{"id":4,"name":"мясо","measurement_unit":"г"},{"id":1,"name":"яйцо","measurement_unit":"шт"}]
## Автор: Елизавета Перевалова 
