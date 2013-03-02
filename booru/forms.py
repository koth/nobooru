# -*- coding: utf-8 -*-
from booru.form_validators import validate_image_data
from booru.upload import images_upload_set, invalid_file_type_message
from flask.ext.wtf import Form, FileField, FileAllowed, FileRequired, TextAreaField, TextField


images_allowed_validator = FileAllowed(upload_set=images_upload_set, message=invalid_file_type_message)


class UploadImageForm(Form):
    html_id = "image-upload-form"

    image = FileField(label="Image file", validators=[FileRequired(), images_allowed_validator, validate_image_data])
    description = TextAreaField(label="Description")
    source_url = TextField(label="URL of source", description="The url of the original page of this image. "
                                                              "This should be something like a gallery page "
                                                              "in a deviantArt gallery, NOT a raw image URL. "
                                                              "Give credit where credit is due!")
    artist_name = TextField(label="Artist")