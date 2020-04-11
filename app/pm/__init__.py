from flask import Blueprint

pm = Blueprint('pm', __name__)

from . import views
