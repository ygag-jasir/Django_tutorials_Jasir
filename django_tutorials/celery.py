# from celery import Celery

# app = Celery('tasks', broker='pyamqp://guest@localhost//')

# @app.task
# def add(x, y):
#     return x + y

import os

from django.conf import settings
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorials.settings')
app = Celery('django_tutorials')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# app.conf.beat_schedule = {
#     # Scheduler Name
#     'expire-transactions': {
#         # Task Name (Name Specified in Decorator)
#         'task': 'celery_task_sample',
#         # Schedule
#         # Execute at: every 1 minute
#         # 'schedule': crontab(minute="*/1"),
#         # every 10 seconds
#         'schedule': 10.0,
#         # Function Arguments
#         'args': ()
#     },
# }


# @app.task(bind=True)
# def debug_task():
#     print(f'Celery task worked at ')
