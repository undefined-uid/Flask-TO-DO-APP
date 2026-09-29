from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password=db.Column(db.String(50), nullable=False)


class Task(db.Model):
    __tablename__="task"

    task_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable=False)
    task = db.Column(db.String(500))
    status = db.Column(db.Boolean, default=False, nullable=False)

