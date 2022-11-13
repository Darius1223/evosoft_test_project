#!/bin/bash

echo "Start celery worker"

celery -A apps.core worker --loglevel=INFO --concurrency=10