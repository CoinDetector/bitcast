from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
from celery.schedules import crontab
from .celery import app
@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="multiply_two_numbers")
def mul(x, y):
    total = x * (y * random.randint(3, 100))
    return total

@task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'add-every-minute-contrab': {
        'task': 'multiply_two_numbers',
        'schedule': crontab(),  # 1분마다
        'args': (16, 16),
    },
    'add-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0,  # 5초마다
        'args': (16, 16)
    },
    'add-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0, # 30초마다
        'args': (16, 16)
    },
}





@task(name="crowling_keyword")
def crowling(x, y):
    total = x * (y * random.randint(3, 100))
    return total




