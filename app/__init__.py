from flask import Flask

wave_finder_app = Flask(__name__)

from app import routes