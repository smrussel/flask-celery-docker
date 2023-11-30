import time
from src.models import TaskResult
from src.extensions import db
from celery import shared_task
from celery.contrib.abortable import AbortableTask
from flask import current_app

@shared_task
def hello_world():
    for i in range(1, 6):
        print(i)
        time.sleep(1)
    tasks = TaskResult.query.all()
    for task in tasks:
        print(task.result)

    print("Hello Celery")


@shared_task(bind=True, base=AbortableTask)
def perform_database_operation(self,data):
    new_record = TaskResult(result=data)
    db.session.add(new_record)
    db.session.commit()
    print("Database operation completed successfully.")
    enqueue_another_function.apply_async(args=[data])
    for i in range(10):
        print(i)
        time.sleep(1)
        if self.is_aborted():
            return 'TASK STOPPED!'
    print(f"database function completed with data: {data}")

@shared_task
def enqueue_another_function(data):
    # Your logic for the function enqueued after the database operation
    print(f"Enqueued function completed with data: {data}")