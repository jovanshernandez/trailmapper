from flask import Blueprint

cm = Blueprint('cm', __name__)

from . import views
