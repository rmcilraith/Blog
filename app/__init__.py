from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

wavefinder_app = Flask(__name__)
wavefinder_app.config.from_object(Config)
db = SQLAlchemy(wavefinder_app)
migrate = Migrate(wavefinder_app, db)

from app import routes, models