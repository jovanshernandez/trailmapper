from flask import Blueprint

fiore = Blueprint('fiore', __name__)

from . import views
