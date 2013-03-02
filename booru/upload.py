# -*- coding: utf-8 -*-
from flask.ext.uploads import UploadSet

allowed_file_extensions = tuple("png jpeg jpg svg gif".split())
images_upload_set = UploadSet("images", allowed_file_extensions)

invalid_file_type_message = "Only the following extensions are allowed: " + ", ".join(allowed_file_extensions)