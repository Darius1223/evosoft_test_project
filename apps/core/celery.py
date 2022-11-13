import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

app = Celery("core", broker=settings.BROKER_URL)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.beat_schedule = {
    "diary_auto_delete_job": {
        "task": "diary_auto_delete_job",
        "schedule": crontab(minute="*/10"),
    },
}


app.autodiscover_tasks()
