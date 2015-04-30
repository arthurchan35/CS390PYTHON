#!/usr/bin/python

import datetime


def patch_html(file, patches):
    s = open(file).read()

    for x in patches:
        s = s.replace(x[0], str(x[1]))
    return s


def default_patches():
    p = [
        ["%date", datetime.datetime.now().strftime("%x")],
        ["%time", datetime.datetime.now().strftime("%X")],


        ]
    return p