from flask import Blueprint

genz = Blueprint('genz', __name__)

from . import views
