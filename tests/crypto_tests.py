# -*- coding: utf8 -*-

import unittest
from crypto import generate_password_hash, password_matches_hash

class CryptoTests(unittest.TestCase):

    passwd = "hunter2"
    utf8_pw = u"๏[-ิิ_•ิ]๏"

    def hash_and_check(self, real_password, attempted_password):
        hashed_password = generate_password_hash(real_password)
        return password_matches_hash(attempted_password, hashed_password)

    def test_can_hash_string(self):
        generate_password_hash(self.passwd)

    def test_can_hash_unicode(self):
        generate_password_hash(unicode(self.passwd))

    def test_can_hash_multibyte_unicode(self):
        generate_password_hash(self.utf8_pw)

    def test_can_verify_password(self):
        self.assertTrue(
            expr=self.hash_and_check(
                real_password=self.passwd,
                attempted_password=self.passwd
            ),
            msg="Password did not match against its own hash!",
        )

    def test_can_verify_unicode_password(self):
        self.assertTrue(
            expr=self.hash_and_check(
                real_password=self.passwd,
                attempted_password=unicode(self.passwd),
            ),
            msg="Unicode version of password didn't match against hash generated from ASCII.",
        )

    def test_can_verify_unicode_against_unicode(self):
        self.assertTrue(
            expr=self.hash_and_check(
                real_password=unicode(self.passwd),
                attempted_password=unicode(self.passwd),
            ),
            msg="Unicode version of password didn't match against hash generated from itself.",
        )

    def test_can_verify_against_unicode_hash(self):
        utf8_hash = unicode(generate_password_hash(self.passwd))
        self.assertTrue(
            expr=password_matches_hash(self.passwd, utf8_hash),
            msg="ASCII password didn't match hash generated from utf8 version of itself.",
        )

    def test_can_verify_multibyte_unicode(self):
        self.assertTrue(
            expr=self.hash_and_check(
                real_password=self.utf8_pw,
                attempted_password=self.utf8_pw
            ),
            msg="UTF-8 password with multibyte characters did not match against its own hash!",
        )

