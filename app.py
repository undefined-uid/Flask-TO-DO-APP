from flask import Flask,render_template,request
from flask_login import login_manager
from models import db, User, Task

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"

db.init_app(app)


@app.route("/", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]

        user = User(name=name,
                    username=username,
                    password=password)

        db.session.add(user)
        db.session.commit()
    return render_template("login.html")
    


with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(debug=True)
