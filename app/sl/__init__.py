from flask import Blueprint

sl = Blueprint('sl', __name__)

from . import views
