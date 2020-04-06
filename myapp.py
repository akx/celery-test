from celery import Celery
import config

celery = Celery("myapp")
celery.conf.update(config.celery_config)


@celery.task
def hello_task(n):
    return " ".join(["hello"] * n)


def hello():
    asr = hello_task.delay(4)
    res = asr.wait(timeout=1)
    return res.upper()


if __name__ == "__main__":
    print(hello())
