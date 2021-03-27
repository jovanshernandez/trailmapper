# app/__init__.py

# third-party imports
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    Bootstrap(app)

    from app import models

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .cm import cm as cm_blueprint
    app.register_blueprint(cm_blueprint, url_prefix='/cm')

    from .th import th as th_blueprint
    app.register_blueprint(th_blueprint, url_prefix='/th')

    from .pm import pm as pm_blueprint
    app.register_blueprint(pm_blueprint, url_prefix='/pm')

    from .sl import sl as sl_blueprint
    app.register_blueprint(sl_blueprint, url_prefix='/sl')

    return app
