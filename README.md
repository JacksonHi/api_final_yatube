# api_final
## Описание

REST API для проекта yatube.

## Запуск проекта

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
cd kittygram
```
Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```
Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
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

## Примеры

Примеры запросов можно посмотреть по ссылке:

```
http://127.0.0.1:8000/redoc/
```
