#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Import this from a python console to get a nice environment for playing with models and such.
"""

import os
import readline
from pprint import pprint

from flask import *

from database import *
from users.models import *
from users.forms import *
import users.constants as USER

from booru.models import *
from booru.forms import *
from app import *

app = create_app()
connect_all(app)

os.environ['PYTHONINSPECT'] = 'True'
