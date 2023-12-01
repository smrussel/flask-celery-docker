from flask import Flask
from src.utils import celery_init_app
from src.extensions import db
import os
# from celery.schedules import crontab

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = 'secret-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://redis",
            result_backend="redis://redis",
            task_ignore_result=True,
            beat_schedule={
                "task-every-10-seconds": {
                    "task": "src.tasks.hello_world",
                    "schedule": 10,
                }
            },
        ),
    )

    db.init_app(app)
    
    app.config.from_prefixed_env()
    celery_init_app(app)
    
    from src.main.routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/")
    # with app.app_context():
    #     db.create_all()
    
    return app