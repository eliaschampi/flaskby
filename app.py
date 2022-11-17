import os
from flask import Flask, render_template, flash, redirect
from loginform import LoginForm
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY") or "secret"
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash ("Inicio de sesión solicitado por {}, ¿Recordar?={}".format(
            form.username.data, form.remember_me.data))
        return redirect("/")
    return render_template("pages/login.html", form=form)




@app.route("/user/<name>")
def userpage(name):
    return render_template("pages/user.html", name=name)

@app.errorhandler(404)
def page_not_found():
    return render_template("pages/404.html")

@app.errorhandler(500)
def page_error():
    return render_template("pages/500.html")

if __name__ == "__main__":
    app.run(port=3002)