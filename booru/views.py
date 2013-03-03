# -*- coding: utf-8 -*-
from fileinput import filename
from booru.forms import UploadImageForm
from booru.models import Image, Artist
from booru.upload import images_upload_set
import config
from flask import (
    Blueprint,
    render_template,
    request,
)
from flask.ext.login import current_user

mod = Blueprint('booru', __name__, static_folder=config.IMAGE_STORAGE_DIRECTORY)


@mod.route('/')
def index():
    return render_template("booru/index.html", user=current_user)


def store_image_file(form, image_id):
    images_upload_set.save(form.image.file, name="%s." % image_id)


def image_from_form(form):
    """
    Create an Image object for database persistance from an UploadImageForm.
    :type form: UploadImageForm
    """
    image = Image(filename=form.image.file.filename, description=form.description.data,
                  source_url=form.source_url.data, user=current_user)

    image.user_ip = request.remote_addr
    image.file_hash = "derp"
    image.width = "1337"
    image.height = "9001"

    artist_name = form.artist_name.data

    if artist_name:
        artist = Artist.get_by_name(artist_name)
        image.artist = artist

    return image


@mod.route('/upload/', methods=['GET', 'POST'])
def upload():
    form = UploadImageForm()
    if form.validate_on_submit():
        image_record = image_from_form(form)
        store_image_file(form, image_record.id)
        image_record.save()

        return "yay, uploaded " + form.image.file.filename

    # Workaround for a bug in Flask-WTF (or maybe WTForms) where the repr of an empty image ends up as the value
    # attribute of the form input when there are errors.
    form.image.data = ""
    return render_template("booru/upload.html", form=form)


@mod.route('/i/<int:image_id>')
def image(image_id):
    image = Image.query.get(image_id)
    uploader = image.user
    artist = Artist(name="KatPainter")

    return render_template("booru/image.html", image=image, artist=artist, uploader=uploader)

