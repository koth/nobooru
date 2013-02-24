# -*- coding: utf-8 -*-

from config import *

DEBUG = True
TESTING = True

ADMINS = frozenset(["admin@admin.lal"])
SECRET_KEY = "super duper secret key"

SQLALCHEMY_DATABASE_URI = "sqlite:///"
DATABASE_CONNECT_OPTIONS = {}
TABLENAME_PREFIX = "test_prefix"

THREADS_PER_PAGE = 4

CSRF_ENABLED = True
CSRF_SESSION_KEY = "csrf session key"

BCRYPT_NUM_ROUNDS = 12
