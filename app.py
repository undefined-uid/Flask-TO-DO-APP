from flask import Flask
from flask_login import login_manager
from models import db, User, Task

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db.init_app(app)

with app.app_context():
    db.create_all()