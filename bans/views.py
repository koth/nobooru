# -*- coding: utf-8 -*-
from flask import Blueprint, request
from bans.models import Ban

mod = Blueprint('bans', __name__, url_prefix='/bans')


@mod.before_app_request
def intercept_if_banned():
    banned = Ban.check_ip_banned(request.remote_addr)
    if banned:
        request.base_url = "/banned"


@mod.route("/banned")
def banned():
    return 1