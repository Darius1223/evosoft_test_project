#!/bin/bash

echo "Start celery beat"

celery -A apps.core beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler