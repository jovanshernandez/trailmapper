# app/spet/__init__.py

from flask import Blueprint

spet = Blueprint('spet', __name__)

from . import views
