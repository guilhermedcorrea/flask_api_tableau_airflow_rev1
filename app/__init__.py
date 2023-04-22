from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
#from dotenv import load_dotenv
#from celery import Celery
from .extensions import db
#load_dotenv()

from .config import SQLALCHEMY_DATABASE, SECRET_KEY


CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL')
RESULT_BACKEND = os.getenv('RESULT_BACKEND')


#celery = Celery(__name__, broker=CELERY_BROKER_URL,
#    result_backend=RESULT_BACKEND) 



db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] =SQLALCHEMY_DATABASE
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #celery.conf.update(app.config)

    db.init_app(app)
 
    migrate.init_app(app, db)

    with app.app_context():
       from .blueprints.api_airflow import airflow_bp
       
       from .blueprints.api_tableau import tableau_bp
       
       app.register_blueprint(airflow_bp)
       app.register_blueprint(tableau_bp)
      
       
    return app