from flask import Flask
from config import Config

wave_finder_app = Flask(__name__)
wave_finder_app.config.from_object(Config)

from app import routes