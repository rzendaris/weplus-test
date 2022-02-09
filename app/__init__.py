import os
import logging
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config, DevelopmentConfig
from app.connection.db import Database
from app.utils.utils import CustomUtils
from logging.handlers import RotatingFileHandler

# app config
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
bootstrap = Bootstrap(app)

# create database
Database.create_db()
app.db = Database()
app.db.delete_read_my_mind()
app.db.create_numbers()

# utils
app.utils = CustomUtils()

from app.errors import bp as errors_bp
from app.fizzbuzz import bp as fizzbuzz_bp
from app.readmymind import bp as readmymind_bp

app.register_blueprint(errors_bp)

app.register_blueprint(fizzbuzz_bp)

app.register_blueprint(readmymind_bp)

# from app import routes

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/weplus-test.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('WePlus startup')