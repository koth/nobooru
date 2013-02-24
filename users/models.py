# -*- coding: utf-8 -*-
import re
from sqlalchemy.exc import IntegrityError
from flask.ext.login import UserMixin

from crypto import generate_password_hash, password_matches_hash
from database import db
from database_errors import UniquenessViolation
import users.constants as USER


class User(db.Model, UserMixin):
    __tablename__ = "users_user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=USER.USER)
    status = db.Column(db.SmallInteger, default=USER.NEW)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def __repr__(self):
        return "<User {self.name}, email={self.email}, id={self.id}>".format(self=self)

    def check_password(self, password):
        return password_matches_hash(password, self.password_hash)

    def save(self):
        db.session.add(self)
        try:
            db.session.commit()
        except IntegrityError, err:
            match = re.match(r"\(IntegrityError\) column (.*) is not unique", err.message)
            raise UniquenessViolation(match.group(1))

    @staticmethod
    def get_by_email(email):
        """
        Look up a User by email. Can implement caching here.
        @param email: User's email.
        @type email: basestring
        @return: User instance
        @rtype: User
        """

        # We make this function so that we can add caching easily later on.
        return User.query.filter(User.email == email).first()

    @staticmethod
    def get_by_username(username):
        """
        Look up a User by username.

        :param username: The username of the User to look up.
        :type username: basestring
        :return: User instance
        :rtype: User
        """
        return User.query.filter(User.name == username).first()

    @staticmethod
    def get_by_id(user_id):
        return User.query.filter(User.id == user_id).first()
