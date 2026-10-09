from flask import Flask,render_template,request,flash,redirect,url_for
from flask_login import LoginManager,login_user, login_required, current_user,logout_user
from models import db, User, Task

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SECRET_KEY"] = "your-secret-key"
login_manager = LoginManager()
login_manager.init_app(app)
db.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods = ["GET","POST"])
def login():
    if request.method == "POST": 
        username = request.form["username"]
        password = request.form["password"]
        
        user = User.query.filter_by(username=username).first()

        if user and user.password==password:
            login_user(user)
            return redirect(url_for("dashboard"))
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


@app.route("/dashboard", methods=["GET","POST"])
@login_required
def dashboard():
    filter_value = request.args.get("filter", "pending")

    if request.method == "POST":
        task_text=request.form["task"]
        new_task= Task(task=task_text,user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()    
    
    
    if filter_value == "pending":
        tasks = Task.query.filter_by(
            status=False,
            user_id=current_user.id
        ).all()

    elif filter_value == "completed":
        tasks = Task.query.filter_by(
            status=True,
            user_id=current_user.id
        ).all()

    else:
        tasks = Task.query.filter_by(
            user_id=current_user.id
        ).all()

    

    return render_template("dashboard.html", tasks=tasks ,filter_value=filter_value)



@app.route("/complete/<int:task_id>", methods=["POST"])
@login_required
def complete_task(task_id):
    task = Task.query.filter_by(
        task_id=task_id,
        user_id=current_user.id
    ).first_or_404()

    task.status = True
    db.session.commit()

    return redirect(url_for("dashboard"))

@app.route("/edit/<int:task_id>", methods=["POST"])
@login_required
def edit_task(task_id):
    task = Task.query.filter_by(
        task_id=task_id,
        user_id=current_user.id
    ).first_or_404()

    task.task = request.form["task"]
    db.session.commit()

    return redirect(url_for("dashboard"))


@app.route ("/tasks", methods=["GET","POST"])
@login_required
def task():
    if request.method == "POST":
        task_text = request.form["task"]
        new_task = Task(task=task_text,user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    return render_template("task.html")

@app.route ("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
    


with app.app_context():
    db.create_all()


if __name__=="__main__":
    app.run(debug=True)
