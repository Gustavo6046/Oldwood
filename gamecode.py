import os
import imp
import errors
import traceback


codefn = "data/code.py"

if os.path.isfile(codefn):
    data = imp.load_source(codefn, "code")

else:
    raise errors.CodeError("Game's code.py file not found!")

def access_code(vname):
    try:
        return getattr(data, vname)

    except AttributeError:
        return None

def game_init():
    preinit = access_code("__preinit__")

    if preinit:
        preinit()

    init = access_code("__init__")

    if init:
        init()

def game_do(fname, *args, **kwargs):
    f = access_code(fname)

    if f:
        f(*args, **kwargs)