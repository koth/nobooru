# -*- coding: utf-8 -*-
from database_errors import UniquenessViolation
from flask.ext.sqlalchemy import SQLAlchemy
import re
from sqlalchemy.exc import IntegrityError

db = SQLAlchemy()


def init_db():
    db.create_all()


def connect_app(app):
    db.app = app
    db.init_app(app)


def rollback():
    db.session.rollback()


class SaveMixin(object):
    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError, err:
            match = re.match(r"\(IntegrityError\) column (.*) is not unique", err.message)
            raise UniquenessViolation(match.group(1))