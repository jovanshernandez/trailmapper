from flask import Blueprint

beyer = Blueprint('beyer', __name__)

from . import views
