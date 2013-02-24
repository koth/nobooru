# -*- coding: utf-8 -*-
from database import db


class Ban(db.Model):
    __tablename__ = "bans_ban"

    id = db.Column(db.Integer, primary_key=True)
    ip_addr = db.Column(db.String(15))


    @staticmethod
    def check_ip_banned(ip_addr):
        """
        Check whether or not a given IP address is banned.

        :param ip_addr: The IP address of the remote user.
        :type ip_addr: basestring
        :return: Whether or not the IP is banned.
        :rtype: bool
        """
        return Ban.query.exists(Ban.ip_addr == ip_addr)