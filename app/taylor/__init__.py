from flask import Blueprint

taylor = Blueprint('taylor', __name__)

from . import views
