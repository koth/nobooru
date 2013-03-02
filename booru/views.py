# -*- coding: utf-8 -*-
from booru.forms import UploadImageForm
from booru.models import Image, Artist
from booru.upload import images_upload_set
import config
from flask import (
    Blueprint,
    render_template
    )
from flask.ext.login import current_user

mod = Blueprint('booru', __name__, static_folder=config.IMAGE_STORAGE_DIRECTORY)


@mod.route('/')
def index():
    return render_template("booru/index.html", user=current_user)


@mod.route('/upload/')
def upload():
    form = UploadImageForm()
    return render_template("booru/upload.html", form=form)

@mod.route('/upload/', methods=['POST'])
def POST_upload():
    form = UploadImageForm()
    if form.validate_on_submit():
        images_upload_set.save(form.image.file)
        return "yay, uploaded " + form.image.file.filename
    else:
        return "nogo"


@mod.route('/i/<int:image_id>')
def image(image_id):
    image = Image.query.get(image_id)
    uploader = image.user
    artist = Artist(name="KatPainter")

    return render_template("booru/image.html", image=image, artist=artist, uploader=uploader)

