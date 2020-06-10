from flask import Flask
from config import Config

wavefinder_app = Flask(__name__)
wavefinder_app.config.from_object(Config)

from app import routes