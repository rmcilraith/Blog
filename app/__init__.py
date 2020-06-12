from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

blog_app = Flask(__name__)
blog_app.config.from_object(Config)
db = SQLAlchemy(blog_app)
migrate = Migrate(blog_app, db)

from app import routes, models