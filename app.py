from flask import Flask,render_template,request,flash
from flask_login import login_manager
from models import db, User, Task

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SECRET_KEY"] = "your-secret-key"
db.init_app(app)


@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST": 
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username).first()

        if user and user.password==password:
            return render_template ("dashboard.html")
        else:
            flash("Invalid username or password")
    return render_template("login.html")


@app.route("/register", methods = ["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]

        new_user = User(name=name,
                    username=username,
                    password=password)

        db.session.add(new_user)
        db.session.commit()
    return render_template("register.html")
    


with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(debug=True)
