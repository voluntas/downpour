#!/usr/bin/env python
import os

from downpour.celery import celery

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'downpour.celery')
    celery.start()
