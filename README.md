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
