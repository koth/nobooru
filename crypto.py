# -*- coding: utf-8 -*-
import bcrypt
from config import BCRYPT_NUM_ROUNDS

def generate_password_hash(password):
    """
    Generates a hash given a plaintext password.

    :param password: A plaintext password.
    :type password: unicode or str
    :return: password hash
    :rtype: str
    """
    return bcrypt.hashpw(
        escape_password(password),
        bcrypt.gensalt(BCRYPT_NUM_ROUNDS)
    )


def password_matches_hash(password, real_hash):
    """
    Checks to see if a given plaintext password would generate a given hash.

    :param password: The purported plaintext password.
    :type password: str or unicode
    :param real_hash: The hash of the real password.
    :type real_hash: str
    :return: True if the password is correct (i.e., matches the hash) and False otherwise.
    :rtype: bool
    """
    attempt_hash = bcrypt.hashpw(
        escape_password(password),
        real_hash,
    )
    return real_hash == attempt_hash


def escape_password(password):
    """
    Encode a password as ASCII text, since some hashing modules have trouble handling python unicode, even UTF-8.
    Currently encodes unicode using XML escaping.

    :param password: String to be encoded in ascii.
    :type password: str or unicode
    :return: The ascii-encoded string.
    :rtype: str
    """
    if isinstance(password, unicode):
        password = password.encode("ascii", "xmlcharrefreplace")
    return password