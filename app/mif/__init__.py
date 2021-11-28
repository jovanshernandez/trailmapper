# app/mif/__init__.py

from flask import Blueprint

mif = Blueprint('mif', __name__)

from . import views
