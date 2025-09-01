from flask import render_template, request, session, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from forms import RegisterForm, MessageForm, LoginForm
from extensions import app, db
from models import Message, User
from datetime import datetime
from werkzeug.security import check_password_hash
import requests
import json



RASA_LINK = "http://127.0.0.1:5005"


@app.context_processor
def inject_forms():
    from forms import LoginForm
    return dict(login_form_obj=LoginForm())


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    form = MessageForm()

    if form.validate_on_submit():
        data = {
            "sender": current_user.username,
            "message": form.message.data
        }
        response = requests.post(f"{RASA_LINK}/webhooks/rest/webhook",
                                 data=json.dumps(data))

        if response.status_code == 200:
            user_message = Message(
                text=form.message.data,
                sent_time=datetime.now(),
                user_id=current_user.id,
                is_chatbot=False
            )
            user_message.create()


            data = response.json()
            if data and len(data) > 0 and "text" in data[0]:
                bot_response = data[0]["text"]
            else:
                bot_response = "Sorry, I didn’t understand that."

            bot_message = Message(
                text=bot_response,
                sent_time=datetime.now(),
                user_id=current_user.id,
                is_chatbot=True
            )
            bot_message.create()

        return redirect(url_for("chat"))  # POST/Redirect/GET


    messages = current_user.messages

    return render_template("chat.html", form=form, messages=messages)


@app.route("/faq")
def faq():
    return render_template("faq.html")


@app.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash("A user with this name already exists. Try a different name.", "danger")
            return redirect(url_for("registration"))

        user = User(username=form.username.data,
                    password=form.password.data,
                    birthday=form.birthday.data,
                    gender=form.gender.data,
                    country=form.country.data)

        user.create()
        flash("Registration completed successfully!", "success")

        logout_user()

        return redirect(url_for("home"))
    return render_template("registration.html", form=form)


@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")





@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            if next:
                return redirect(next)
            return redirect(url_for("home"))

    return render_template("login.html", form=form)


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
