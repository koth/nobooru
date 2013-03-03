# -*- coding: utf-8 -*-
from datetime import datetime
from database import db, SaveMixin


class Image(db.Model, SaveMixin):
    __tablename__ = "booru_image"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users_user.id"))
    filename = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text(), default="", nullable=False)
    user_ip = db.Column(db.Integer)
    file_hash = db.Column(db.String(128), nullable=False)
    upload_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    modified_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey("booru_artist.id"))
    source_url = db.Column(db.String, default="", nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)

    user = db.relationship("User", backref="image")
    artist = db.relationship("Artist", backref="image")

    def __init__(self, filename, description, source_url, user):
        self.filename = filename
        self.description = description
        self.source_url = source_url
        self.user = user


class Artist(db.Model):
    __tablename__ = "booru_artist"

    """
    Reminder: Put an index on name and user_id.
    """

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users_user.id"))
    files = db.Column(db.Integer, nullable=False)
    site = db.Column(db.String(500))
    removed = db.Column(db.Boolean, default=False, nullable=False)
    up = db.Column(db.Integer, default=0, nullable=False)
    down = db.Column(db.Integer, default=0, nullable=False)

    user = db.relationship("User", backref="artist", uselist=False)


class Comment(db.Model):
    __tablename__ = "booru_comment"

    id = db.Column(db.Integer, primary_key=True)
    file_id = db.Column(db.Integer, db.ForeignKey("booru_image.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users_user.id"), nullable=False)
    # Denormalized author column. Do we really need this? With caching and stuff, we won't make the actual queries
    # that often at all.
    author = db.Column(db.String(30), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    ip = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    removed = db.Column(db.Boolean, nullable=False, default=False)

    user = db.relationship("User", backref="comment")
