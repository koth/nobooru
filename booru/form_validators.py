# -*- coding: utf-8 -*-


def validate_image_data(form, field):
    if field.file:
        field.file.filename

        # raise ValidationError if bad
