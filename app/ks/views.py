# app/ks/views.py

from flask import abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_required, LoginManager, UserMixin, login_user, current_user

from . import ks
from app import models, db
from app.models import Employee

department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))


@ks.route('/')
def homepage():
    """
    Render the thpage template on the / route
    """
    return render_template('ks/index.html', title="Welcome")

@ks.route('/dashboard1')
@login_required
def dashboard1():
    """
    Render the dashboard template on the /dashboard1 route
    """
    ee = Employee.query.filter_by(department_id=23).first() 
    return render_template('ks/dashboard1.html', title="Dashboard1")

@ks.route('/dashboard2')
@login_required
def dashboard2():
    """
    Render the dashboard template on the /dashboard2 route
    """
    ee = Employee.query.filter_by(department_id=23).first()
    return render_template('ks/dashboard2.html', title="Dashboard2")

@ks.route('/dashboard3')
@login_required
def dashboard3():
    """
    Render the dashboard template on the /dashboard3 route
    """
    return render_template('ks/dashboard3.html', title="Dashboard3")

@ks.route('/dashboard4')
@login_required
def dashboard4():
    """
    Render the dashboard template on the /dashboard4 route
    """
    return render_template('ks/dashboard4.html', title="Dashboard4")    