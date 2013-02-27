# -*- coding: utf-8 -*-
import datetime
from booru.models import Image, Artist
from flask import (
    Blueprint,
    render_template,
)
from flask.ext.login import current_user
from users.models import User

mod = Blueprint('booru', __name__)


@mod.route('/')
def index():
    return render_template("booru/index.html", user=current_user)


@mod.route('/upload/')
def upload():
    return render_template("booru/upload.html")


@mod.route('/i/<int:image_id>')
def image(image_id):
    image = Image.query.get(image_id)
    uploader = image.user
    artist = Artist(name="KatPainter")

    return render_template("booru/image.html", image=image, artist=artist, uploader=uploader)

