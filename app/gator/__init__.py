from flask import Blueprint

gator = Blueprint('gator', __name__)

from . import views
