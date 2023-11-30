from flask import Blueprint, render_template, flash, \
    redirect, url_for, current_app
from src.tasks import perform_database_operation
from src.models import TaskResult
user_bp = Blueprint("user_bp", __name__)

@user_bp.route('/')
def index_view():
    return f'Hello application'


@user_bp.route('/add_task/<data>')
def add_task(data):
    # Trigger Celery task
    print('add task data:',data)
    perform_database_operation.delay(data)
    return f'Task added for data: {data}'

@user_bp.route('/get_task')
def get_task():
    # Trigger Celery task
    tasks = TaskResult.query.all()
    for task in tasks:
        print(task.result)
    return f'Task get for data: '


@user_bp.route("/cancel/<task_id>")
def cancel(task_id):
    task = perform_database_operation.AsyncResult(task_id)
    task.abort()
    return "CANCELED!"