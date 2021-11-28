# app/rgz/__init__.py

from flask import Blueprint

rgz = Blueprint('rgz', __name__)

from . import views
