from flask import Blueprint

wrs1 = Blueprint('wrs1', __name__)

from . import views
