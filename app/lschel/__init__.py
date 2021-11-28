from flask import Blueprint

lschel = Blueprint('lschel', __name__)

from . import views
