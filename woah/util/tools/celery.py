import os

from celery import Celery

# from kombu import Queue

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "woah.settings")

app = Celery("woah")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.worker_cancel_long_running_tasks_on_connection_loss = True
# app.conf.task_create_missing_queues = False
app.conf.task_default_queue = "default"
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


def purge_queue(queue_name: str):
    with app.connection_for_write() as conn:
        ret = conn.default_channel.queue_purge(queue_name)
    return ret