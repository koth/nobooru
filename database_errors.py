# -*- coding: utf-8 -*-


class UniquenessViolation(Exception):
    def __init__(self, column_name):
        self.column_name = column_name
        msg = "Uniqueness constraint on column {} was violated.".format(column_name)
        Exception.__init__(self, msg)