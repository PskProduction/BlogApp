# Описание проекта
Блог сайт DjangoRESTFramework + Vue, на главной странице которого отображается список постов.

## Контракт для API
Названия роутов и ожидаемую структуру ответа от API endpoints можно найти в спецификации по адресу ниже (проект 
при этом должен быть запущен):
```http request
/api/schema/swagger
```
## Настройка проекта для работы

```bash
pip install -r requirements.txt
npm run build
```

## Подготовка базы данных
Запуск миграций:
```bash
python manage.py makemigrations
python manage.py migrate
```
Инициализация суперпользователя:
```bash
python manage.py createsuperuser
```

## Запуск проекта
```bash
 python manage.py runserver
```