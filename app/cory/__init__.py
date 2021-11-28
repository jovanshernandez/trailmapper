from flask import Blueprint

cory = Blueprint('cory', __name__)

from . import views
