# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
    current_app,
)
from flask.ext.login import login_user, login_required, logout_user, current_user

import database
from database_errors import UniquenessViolation
from users.constants import LOGIN_WELCOME_MESSAGE, INVALID_CREDS
from users.forms import LoginForm, RegisterForm
from users.models import User


mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/profile/')
@login_required
def profile():
    return render_template('users/profile.html', user=current_user)


@mod.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)

    # If form contains valid data (not necessarily good creds)...
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)

        if user and user.check_password(form.password.data):
            login_user(user)
            flash(LOGIN_WELCOME_MESSAGE.format(username=user.name))
            # If the user was redirected to this page from a page that requires being logged in,
            # then the query parameter `next` will hold the next URL to go to.
            next_url = request.args.get("next") or url_for("users.profile")
            return redirect(next_url)

        flash(INVALID_CREDS, "error-message")

    # By passing the form into the template, we refill the fields with the values the user provided, if any.
    return render_template('users/login.html', form=form)


@mod.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for(current_app.config.get("REDIRECT_AFTER_LOGOUT", "users.login")))


@mod.route("/register/", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        # Create new User instance
        user = User(
            name=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        try:
            user.save()
        except UniquenessViolation, err:
            if err.column_name == "email":
                form.email.errors.append("There is already an account registered with that email address.")
            elif err.column_name == "name":
                form.username.errors.append("There is already an account registered with that username.")
        else:
            login_user(user)

            # Flash a message that gets displayed only once.
            flash("Welcome to the herd.")

            return redirect(url_for("users.profile"))
        finally:
            database.rollback()

    return render_template("users/register.html", form=form)
