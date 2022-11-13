## Тестовый проект EvoSoft

Тестовое задание Django

---

### Contributors (telegram):

* @Darius1223

---

### Запуск проекта

#### Docker experience:

1. Поднимаем проект, путем:

```shell
docker-compose up --build
```

2. Ждем сборки образа, приложение доступно по `http://locahost:8000/`

#### venv experience (локально):

1. Создаем и активируем виртуальное окружение:

```shell
python -m venv venv
# for linux
source venv/bin/activate
# for windows
venv/Scripts/activate.bat
```

2. Добавляем переменные окружения. Создаем `.env` файл со следующим содержимым:

```dotenv
DATABASE_URL= # адрес базы данных
DJANGO_SETTINGS_MODULE= # конфигурационный файл django, напр. config.setting.local
```

3. Устанавливаем зависимости (локально):

```shell
pip install -r requirements/local.txt
```

4. Запускаем django приложение:

```shell
python manage.py runserver
```

5. Поднимаем celery окружение (в разных терминалах):

```shell
celery -A apps.core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
celery -A apps.core flower --port=5555 --address=0.0.0.0
celery -A apps.core worker --loglevel=INFO --concurrency=10
```

6. Приложение доступно по `http://locahost:8000/`, flower по `http://locahost:5555/`
