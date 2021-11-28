from flask import Blueprint

staples = Blueprint('staples', __name__)

from . import views
