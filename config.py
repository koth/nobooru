# -*- coding: utf-8 -*-
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(["mantavia@octabooru.net", "horsemilk@octabooru.net"])
SECRET_KEY = "do whatever you want"

SQLITE_DB_FILE = "app.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(_basedir, SQLITE_DB_FILE)
DATABASE_CONNECT_OPTIONS = {}
TABLENAME_PREFIX = "caballus"

THREADS_PER_PAGE = 4

CSRF_ENABLED = True
CSRF_SESSION_KEY = "I am not a secure key. Wait, am I? Not if I am in the repo, anyway."

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = "huh"
RECAPTCHA_PRIVATE_KEY = "what"
RECAPTCHA_OPTIONS = {"theme": "white"}

BCRYPT_NUM_ROUNDS = 12

LOGIN_REQUIRED_MESSAGE = "You'll need to log in to access this page, chum."
LOGIN_VIEW = "users.login"

BOOTSTRAP_CUSTOM_CSS = True
