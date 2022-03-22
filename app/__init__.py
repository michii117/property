from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import views

from flask_migrate import Migrate 
migrate = Migrate(app, db)

