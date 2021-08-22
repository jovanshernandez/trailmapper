from flask import Blueprint

blak = Blueprint('blak', __name__)

from . import views
