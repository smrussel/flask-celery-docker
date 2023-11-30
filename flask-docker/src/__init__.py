from flask import Flask
from src.utils import make_celery
from src.extensions import db
import os
from celery.schedules import crontab

basedir = os.path.abspath(os.path.dirname(__file__))

def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = 'secret-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["CELERY_CONFIG"] = {
        "broker_url": "redis://redis", 
        "result_backend": "redis://redis", 
        "beat_schedule": {
            "task-every-10-seconds" : {
                "task": "src.tasks.hello_world",
                "schedule": 10,
                #"args": (1, 2)
            }
        }   
    }

    db.init_app(app)
    celery = make_celery(app)
    celery.set_default()
    
    from src.main.routes import user_bp
    app.register_blueprint(user_bp, url_prefix="/")
    # with app.app_context():
    #     db.create_all()
    
    return app, celery