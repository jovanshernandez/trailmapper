# app/pp/__init__.py

from flask import Blueprint

pp = Blueprint('pp', __name__)

from . import views
