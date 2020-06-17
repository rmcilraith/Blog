from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

blog_app = Flask(__name__)
blog_app.config.from_object(Config)
db = SQLAlchemy(blog_app)
migrate = Migrate(blog_app, db)
login = LoginManager(blog_app)
login.login_view = 'login'

from app import routes, models