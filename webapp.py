"""Flask Login Example and instagram fallowing find"""

from flask import Flask, url_for, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
import models
from db import db
import settings
from flask_admin import Admin
from adminviews import MyModelView
from lm import login_manager
from controllers import home, auth

def setup_app():
    app = Flask(__name__)
    app.secret_key = settings.SECRET
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.ALCHEMY_URL
    db.init_app(app)
    login_manager.init_app(app)

    admin = Admin(app, name='Admin', template_mode='bootstrap3')

    admin.add_view(MyModelView(models.User, db.session,
                            column_list=['id', 'name', "description", "is_active", "is_admin"],
                            search_fields=['username'],
                            form_columns=['id', 'name', "description", "is_active", "is_admin"]))
    app.register_blueprint(home.home)
    app.register_blueprint(auth.auth)

    return app



application = setup_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    application.run('0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', False))
