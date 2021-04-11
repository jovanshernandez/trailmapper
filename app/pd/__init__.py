from flask import Blueprint

pd = Blueprint('pd', __name__)

from . import views
