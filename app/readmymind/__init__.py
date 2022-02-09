from flask import Blueprint

bp = Blueprint('readmymind', __name__)

from app.readmymind import routes