from flask import Blueprint

wrs3 = Blueprint('wrs3', __name__)

from . import views
