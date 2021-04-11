from flask import Blueprint

sab = Blueprint('sab', __name__)

from . import views
