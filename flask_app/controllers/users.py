from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User


#TEMPLATE ROUTES
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/account')
def account():
    if "user_id" in session:
        user = User.get_user_by_id({ "id": session["user_id"] })
        return render_template("account.html", user=user)
    return render_template("account.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")





#ACTION ROUTES
@app.route('/create-account', methods=['POST'])
def create_account():
    if User.validate_registry(request.form):
        User.create_user(request.form)
        data = { "email": request.form["email"] }
        user = User.get_user_by_email(data)
        session['user_id'] = user.id
        return redirect('/account')
    return redirect('/account')

@app.route('/sign-in', methods=['POST'])
def signin():
    data = { "email": request.form["email"] }
    user = User.get_user_by_email(data)
    if not user:
        flash("Invalid Email/Password", "signin")
        return redirect('/account')
    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid Email/Password", "signin")
        return redirect('/account')
    session['user_id'] = user.id
    return redirect('/account')

@app.route('/sign-out')
def signout():
    session.clear()
    return redirect('/account')