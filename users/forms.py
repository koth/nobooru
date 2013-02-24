# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Email, EqualTo, DataRequired
import users.constants as USER

# TODO: Look into using selenium for automated tests.



class LoginForm(Form):
    html_id = "user-login-form"

    email = TextField("Email address", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])


class RegisterForm(Form):
    html_id = "user-registration-form"

    username = TextField("Nickname", [DataRequired()])
    email = TextField("Email address", [DataRequired(), Email()])
    password = PasswordField("Password", [DataRequired()])
    confirm = PasswordField(
        label="Repeat password",
        validators=[
            DataRequired(),
            EqualTo(
                fieldname="password",
                message=USER.PASSWORDS_DO_NOT_MATCH,
            ),
        ],
    )
    accept_tos = BooleanField(USER.TOS_AGREEMENT, [DataRequired()])
#    recaptcha = RecaptchaField()