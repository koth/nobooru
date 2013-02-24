# -*- coding: utf-8 -*-
from flask.ext.testing import TestCase
from app import create_app, connect_all
from database import db
from tests import testing_config


class BaseTest(TestCase):
    """
    The base test case for all Caballus tests.
    """

    def _pre_setup(self):
        """
        A hack to get some autocompletion in PyCharm.
        """
        super(BaseTest, self)._pre_setup()
        #: :type: flask.Flask
        self.app = self.app
        #: :type: flask.testing.FlaskClient
        self.client = self.client

    def create_app(self):
        app = create_app(testing_config)
        connect_all(app)
        return app

    def setUp(self):
        # TODO: Store a common database starting point in a file, copy that to a new .db file, then config the app to
        # use the copy for the test, then destroy it afterwards. New copy of the database for each test rather than
        # creating it all from scratch each time.
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()