#!/bin/bash

echo "Start celery beat"

celery -A apps.core flower --port=5555 --address=0.0.0.0