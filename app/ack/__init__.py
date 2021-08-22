from flask import Blueprint

ack = Blueprint('ack', __name__)

from . import views
