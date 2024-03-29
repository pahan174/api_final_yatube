## Использованный стэк технологий
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)


### Описание проекта

Дынный проект написан в рамках выполнения итогового задания спирнта №10 в курсе Python-разработчик от Яндекс Практикума.
Проект решает задачу предоставления API интерфейса для работы с социальной сетью Yatube.
Через данный API интерфейс возможно создание сторонних приложений и WEB интерфейсов для данной соц. сети.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/pahan174/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Управление пользователями

Пользователяи создаются только из панели Администратора суперпользователя.
Создать суперпользховтеля через комсанду:

```
python3 manage.py createsuperusers
```

### Описание работы и примеры

После запуска сервера документация находится по адресу:

http://127.0.0.1:8000/redoc/

## Примеры запросов к API

Получить список всех публикаций:

```
GET-запрос
http://127.0.0.1:8000/api/v1/posts/
```

Создать публикацию:

```
POST-запрос
http://127.0.0.1:8000/api/v1/posts/
```

Создать комментарий к публикации с ID=1:

```
POST-запрос
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

## Получение JWT токенов

Работа с опасными методами API возможна только с помощью JWT токенов.

Получить JWT-токен

```
POST-запрос
http://127.0.0.1:8000/api/v1/jwt/create/
```




