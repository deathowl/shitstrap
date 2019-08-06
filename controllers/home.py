from flask import Blueprint, render_template
from flask_login import login_required, current_user

home = Blueprint('main', __name__)

@home.route('/')
def index():
    return render_template('index.html')

@home.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
