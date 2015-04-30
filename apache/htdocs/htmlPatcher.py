#!/usr/bin/python

import datetime


def patch_html(file, patches):
    return patch(open(file).read(), patches)


def patch(text, patches):
    if '%' not in text:
        return text       # nothing to replace

    for x in patches:
        m = x[0]
        p = str(x[1])

        text = text.replace(m, p)
        patch(text, patches)
    return text


def default_patches():
    p = [
        ["%date", datetime.datetime.now().strftime("%x")],
        ["%time", datetime.datetime.now().strftime("%X")],


        ]
    return p