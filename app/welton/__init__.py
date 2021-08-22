from flask import Blueprint

welton = Blueprint('welton', __name__)

from . import views
