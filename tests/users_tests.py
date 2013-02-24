from flask import url_for
from flask.ext.login import current_user
from tests.base_test_case import BaseTest
from tests.html_utils import HTMLDocument
from users.forms import RegisterForm, LoginForm
from users.models import User


class UsersTest(BaseTest):

    def test_can_access_login_page(self):
        response = self.client.get(url_for("users.login"))
        self.assert200(response)

    def register_new_user(self, username, email, password, confirm=None, accept_tos=1):
        response = self.client.get(url_for("users.register"))
        self.assert200(response)
        html = HTMLDocument.from_response(response)
        csrf_token = html.form(RegisterForm).fields["csrf_token"]

        response = self.client.post(url_for("users.register"),
            # follow_redirects=True,
            data={
                "csrf_token": csrf_token,
                "username": username,
                "email": email,
                "password": password,
                "confirm": confirm or password,
                "accept_tos": accept_tos,
            }
        )

        return response

    def test_register_new_user(self):
        """
        Register a new user and assert that they're in the database.
        """
        password = "Test driven development is best development. :V"
        expected_user = User(
            name="testo",
            email="testo@test.com",
            password=password,
        )

        nonexistent_user = User.get_by_email(expected_user.email)

        self.assertIsNone(nonexistent_user)

        response = self.register_new_user(expected_user.name, expected_user.email, password)

        self.assert_successful_registration(response)

        actual_user = User.get_by_email(expected_user.email)

        self.assertTrue(actual_user.check_password(password))
        self.assertEqual(actual_user.email, expected_user.email)
        self.assertEqual(actual_user.name, expected_user.name)

    def login_user(self, email, password):
        login_url = url_for("users.login")
        response = self.client.get(login_url)
        html = HTMLDocument.from_response(response)
        csrf_token = html.form(LoginForm).fields["csrf_token"]

        response = self.client.post(login_url,
#            follow_redirects=True,
            data={
                "csrf_token": csrf_token,
                "email": email,
                "password": password,
            },
        )

        self.assert_redirects(response, url_for("users.profile"))

        return response

    def logout_user(self):
        resp = self.client.get(url_for("users.logout"))
        return resp

    def assert_successful_registration(self, response):
        self.assert_redirects(response, url_for("users.profile"))

    def test_login_new_user(self):
        """
        Register a new user, log them in, view the profile
        """
        username = "foomanchu"
        password = "ducks"
        email = "killall@humans.com"

        profile_url = url_for("users.profile")

        resp = self.client.get(profile_url)
        self.assert_redirects(resp, url_for("users.login", next=url_for("users.profile")))

        response = self.register_new_user(username, email, password)

        self.assert_successful_registration(response)

        resp = self.client.get(profile_url)
        self.assert200(resp)

        self.logout_user()

        with self.client:
            self.assertRaises(AttributeError, lambda: current_user.is_authenticated())
            self.login_user(email, password)
            self.assertTrue(current_user.is_authenticated())

        self.logout_user()

        resp = self.client.get(profile_url)
        self.assert_redirects(resp, url_for("users.login", next=url_for("users.profile")))

    def assert_input_has_error(self, resp, input_id):
        html = HTMLDocument.from_response(resp)
        self.assertTrue("has_error" in html.xpath("//input[@id='"+input_id+"']/@class")[0])

    def test_register_email_taken(self):
        username = "bob"
        password = "what"
        email = "what@what.com"

        resp = self.register_new_user(
            username=username,
            password=password,
            email=email,
        )
        self.assert_successful_registration(resp)

        self.logout_user()

        resp = self.register_new_user(
            username="fred",
            password=password,
            email=email,
        )
        self.assert200(resp)
        self.assert_input_has_error(resp, "email")

    def test_register_username_taken(self):
        username = "bob"
        password = "what"
        email = "what@what.com"

        resp = self.register_new_user(
            username=username,
            password=password,
            email=email,
        )
        self.assert_successful_registration(resp)

        self.logout_user()

        resp = self.register_new_user(
            username="bob",
            password=password,
            email="different@mail.com",
        )
        self.assert200(resp)
        self.assert_input_has_error(resp, "username")

    def test_get_user_by_id(self):
        username = "bob"
        password = "what"
        email = "what@what.com"

        resp = self.register_new_user(
            username=username,
            password=password,
            email=email,
        )
        self.assert_successful_registration(resp)

        user = User.get_by_email("what@what.com")
        user_by_id = User.get_by_id(user.id)

        self.assertEqual(user.id, user_by_id.id)
        self.assertEqual(user.email, user_by_id.email)

    def test_bad_passwords(self):
        resp = self.register_new_user(
            username="what",
            password="foo",
            confirm="bar",
            email="what@whatever.com",
        )
        # TODO: These need to actually check the contents of the response data...
        # Why is this hard? Some weird unicode thing. I thought I fixed that, though...
        self.assert200(resp)

        self.assert_input_has_error(resp, "confirm")
