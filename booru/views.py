# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
)
from flask.ext.login import current_user

mod = Blueprint('booru', __name__)


@mod.route('/')
def index():
    return render_template("booru/index.html", user=current_user)


@mod.route('/upload/')
def upload():
    return render_template("booru/upload.html")


@mod.route('/i/<image_id>')
def image(image_id):
    return render_template("booru/image-view.html", **locals())

