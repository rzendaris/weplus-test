from flask import Blueprint

bp = Blueprint('fizzbuzz', __name__)

from app.fizzbuzz import routes