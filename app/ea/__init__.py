# app/ea/__init__.py

from flask import Blueprint

ea = Blueprint('ea', __name__)

from . import views
