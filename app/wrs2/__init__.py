from flask import Blueprint

wrs2 = Blueprint('wrs2', __name__)

from . import views
