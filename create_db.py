from db import db
from webapp import setup_app
db.create_all(app=setup_app())
