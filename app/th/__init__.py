# app/th/__init__.py

from flask import Blueprint

th = Blueprint('th', __name__)

from . import views
