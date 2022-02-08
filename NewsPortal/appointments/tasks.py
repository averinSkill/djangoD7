from celery import shared_task
import time

# проверка работы селери из Д7.4
@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

