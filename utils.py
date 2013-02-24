# -*- coding: utf-8 -*-
import inspect
from config import TABLENAME_PREFIX


def db_prefix(table_name):
    return "{0}_{1}".format(TABLENAME_PREFIX, table_name)


def is_mod_function(mod, func):
    return inspect.isfunction(func) and inspect.getmodule(func) == mod


def list_module_functions(mod):
    return [func for func in mod.__dict__.itervalues() if is_mod_function(mod, func)]
