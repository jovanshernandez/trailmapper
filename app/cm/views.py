# app/cm/views.py

from flask import abort, render_template
from flask_login import current_user, login_required

from . import cm

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

@cm.route('/')
def homepage():
    """
    Render the cmpage template on the / route
    """
    return render_template('cm/index.html', title="Welcome")

@cm.route('/dashboard1')
@login_required
def dashboard1():
    """
    Render the dashboard template on the /dashboard1 route
    """
    return render_template('cm/dashboard1.html', title="Dashboard1")

@cm.route('/dashboard2')
@login_required
def dashboard2():
    """
    Render the dashboard template on the /dashboard2 route
    """
    return render_template('cm/dashboard2.html', title="Dashboard2")

@cm.route('/dashboard3')
@login_required
def dashboard3():
    """
    Render the dashboard template on the /dashboard3 route
    """
    return render_template('cm/dashboard3.html', title="Dashboard3")