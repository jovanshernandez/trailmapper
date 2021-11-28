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

    from .pd import pd as pd_blueprint
    app.register_blueprint(pd_blueprint, url_prefix='/pd')

    from .sab import sab as sab_blueprint
    app.register_blueprint(sab_blueprint, url_prefix='/sab')

    from .ack import ack as ack_blueprint
    app.register_blueprint(ack_blueprint, url_prefix='/ack')

    from .mon import mon as mon_blueprint
    app.register_blueprint(mon_blueprint, url_prefix='/mon')

    from .blak import blak as blak_blueprint
    app.register_blueprint(blak_blueprint, url_prefix='/blak')

    from .genz import genz as genz_blueprint
    app.register_blueprint(genz_blueprint, url_prefix='/genz')

    from .gator import gator as gator_blueprint
    app.register_blueprint(gator_blueprint, url_prefix='/gator')

    from .welton import welton as welton_blueprint
    app.register_blueprint(welton_blueprint, url_prefix='/welton')

    from .wrs1 import wrs1 as wrs1_blueprint
    app.register_blueprint(wrs1_blueprint, url_prefix='/wrs1')

    from .wrs2 import wrs2 as wrs2_blueprint
    app.register_blueprint(wrs2_blueprint, url_prefix='/wrs2')

    from .wrs3 import wrs3 as wrs3_blueprint
    app.register_blueprint(wrs3_blueprint, url_prefix='/wrs3')

    from .ks import ks as ks_blueprint
    app.register_blueprint(ks_blueprint, url_prefix='/ks')

    from .lschel import lschel as lschel_blueprint
    app.register_blueprint(lschel_blueprint, url_prefix='/lschel')

    from .spet import spet as spet_blueprint
    app.register_blueprint(spet_blueprint, url_prefix='/spet')

    from .rgz import rgz as rgz_blueprint
    app.register_blueprint(rgz_blueprint, url_prefix='/rgz')

    from .mif import mif as mif_blueprint
    app.register_blueprint(mif_blueprint, url_prefix='/mif')
    
    from .pp import pp as pp_blueprint
    app.register_blueprint(pp_blueprint, url_prefix='/pp')

    from .ea import ea as ea_blueprint
    app.register_blueprint(ea_blueprint, url_prefix='/ea')

    from .fiore import fiore as fiore_blueprint
    app.register_blueprint(fiore_blueprint, url_prefix='/fiore')

    from .taylor import taylor as taylor_blueprint
    app.register_blueprint(taylor_blueprint, url_prefix='/taylor')

    from .staples import staples as staples_blueprint
    app.register_blueprint(staples_blueprint, url_prefix='/staples')

    from .cory import cory as cory_blueprint
    app.register_blueprint(cory_blueprint, url_prefix='/cory')

    from .beyer import beyer as beyer_blueprint
    app.register_blueprint(beyer_blueprint, url_prefix='/beyer')

    return app
