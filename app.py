# -*- coding: utf-8 -*-
from flask import render_template
from flask import Flask
import sys
import os


def create_app(config="config"):
    """
    Creates a new instance of the web application and registers a couple top-level routes.

    :param config: Object whose attributes will be used as the configuration settings.
    :return: an application instance.
    :rtype: Flask
    """
    app = Flask(__name__)
    app.config.from_object(config)

    from flask.ext.bootstrap import Bootstrap
    Bootstrap(app)

    from users.views import mod as users
    app.register_blueprint(users)
    from booru.views import mod as booru
    app.register_blueprint(booru)

    @app.route("/test")
    def hello_world():
        return "Hello world!"

    @app.errorhandler(404)
    def file_not_found(error):
        # TODO: Log the error.
        return render_template("404.html"), 404

    return app


def connect_db(app):
    import database
    database.connect_app(app)


def connect_login_manager(app):
    import login
    login.connect_app(app)


def connect_converters(app):
    import converters
    converters.RegexConverter.register(app)


def connect_all(app):
    """
    Call every connect_FOO() function defined in this module.

    These connect_FOO() functions are for connecting things to the Flask instance.
    I'm not sure how I feel about this design decision. Sure, it saves you from having to explicitly enable things...
    Is that so bad, though?
    """
    import inspect
    from utils import list_module_functions

    own_name = inspect.stack()[1][3] # Name of the current function
    for func in list_module_functions(sys.modules[__name__]):
        func_name = func.__name__
        if func_name.startswith("connect_") and func_name != own_name:
            func(app)

