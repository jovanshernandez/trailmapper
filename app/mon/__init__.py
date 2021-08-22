from flask import Blueprint

mon = Blueprint('mon', __name__)

from . import views
