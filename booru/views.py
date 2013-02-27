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


@mod.route('/i/<image_id>')
def image(image_id):
    image = Image(
        filename="http://placekitten.com/800/600",
        description="What a wonderfoo world.",
        file_hash="foo",
        upload_time=datetime.datetime(year=2013, month=2, day=12, hour=13, minute=37),
        width=800,
        height=600,
        source_url="http://deviantart.com/whathuh",
    )

    artist = Artist(
        name="KatPainter",
    )

    uploader = User(
        name="Horsefly",
        email="foo@foo.com",
        password="foo",
    )


    return render_template("booru/image.html", image=image, artist=artist, uploader=uploader)

