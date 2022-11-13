import datetime

from celery import shared_task
from loguru import logger

from apps.core import models
from apps.core.utils import job_logger


@shared_task(name="diary_auto_delete_job")
@job_logger
def diary_auto_delete_job():
    models.Diary.objects.filter(expiration__lte=datetime.datetime.now()).delete()
    logger.info("Expired diaries was deleted")
