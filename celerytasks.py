# celery -A celerytasks worker -linfo
from random import randint
from time import sleep

from celery import Celery

celery = Celery('tasks', broker='amqp://guest@localhost//', backend='amqp')

@celery.task
def multiply_line(line, n):
    sleep(randint(1, 8))
    return [line * (i + 1) for i in range(n)]