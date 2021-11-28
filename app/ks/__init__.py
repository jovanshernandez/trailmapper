from flask import Blueprint

ks = Blueprint('ks', __name__)

from . import views
