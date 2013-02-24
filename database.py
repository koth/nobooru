# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db():
    db.create_all()


def connect_app(app):
    db.app = app
    db.init_app(app)


def rollback():
    db.session.rollback()
