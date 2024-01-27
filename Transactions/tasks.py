from datetime import datetime
from celery import shared_task


@shared_task(name='celery_task_sample')
def celery_task_sample():
    print('celery_task_sample from Transaction executed at : '+str(datetime.now()))


@shared_task(name='counter_5')
def counter_5(**kwargs):

    limit = kwargs.get('limit', 1)
    print('counter_5 from Transaction executed at : ' +
          str(datetime.now())+"limit: "+str(limit))
