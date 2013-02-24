# -*- coding: utf-8 -*-
from flask.ext.login import LoginManager
from users.models import User

login_manager = LoginManager()


def connect_app(app):
    login_manager.login_view = app.config.get("LOGIN_VIEW")
    login_manager.login_message = app.config.get("LOGIN_REQUIRED_MESSAGE")
    login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    """
    Load a user by id.

    @param user_id: primary key for user
    @type user_id: unicode
    @return: User instance corresponding to user_id, or None if no such user exists.
    @rtype: User
    """
    return User.get_by_id(user_id)


