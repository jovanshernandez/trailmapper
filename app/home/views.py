# app/home/views.py

from flask import abort, render_template
from flask_login import current_user, login_required

from . import home


@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard1')
@login_required
def dashboard1():
    """
    Render the dashboard template on the /dashboard1 route
    """
    return render_template('home/dashboard1.html', title="Dashboard1")

@home.route('/dashboard2')
@login_required
def dashboard2():
    """
    Render the dashboard template on the /dashboard2 route
    """
    return render_template('home/dashboard2.html', title="Dashboard2")

@home.route('/dashboard3')
@login_required
def dashboard3():
    """
    Render the dashboard template on the /dashboard3 route
    """
    return render_template('home/dashboard3.html', title="Dashboard3")

@home.route('/dashboard3')
@login_required
def dashboard4():
    """
    Render the dashboard template on the /dashboard4 route
    """
    return render_template('home/dashboard4.html', title="Dashboard4")    