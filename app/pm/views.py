# app/pm/views.py

from flask import abort, render_template
from flask_login import current_user, login_required

from . import pm

@pm.route('/')
def homepage():
    """
    Render the pmpage template on the / route
    """
    return render_template('pm/index.html', title="Welcome")

@pm.route('/dashboard1')
@login_required
def dashboard1():
    """
    Render the dashboard template on the /dashboard1 route
    """
    return render_template('pm/dashboard1.html', title="Dashboard1")

@pm.route('/dashboard2')
@login_required
def dashboard2():
    """
    Render the dashboard template on the /dashboard2 route
    """
    return render_template('pm/dashboard2.html', title="Dashboard2")

@pm.route('/dashboard3')
@login_required
def dashboard3():
    """
    Render the dashboard template on the /dashboard3 route
    """
    return render_template('pm/dashboard3.html', title="Dashboard3")