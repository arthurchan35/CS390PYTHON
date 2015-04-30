#!/usr/bin/python

import datetime


def patch_html(file, patches):
    return patch(open(file).read(), patches)


def patch(text, patches):
    b = False
    save = text
    for x in patches:
        m = x[0]
        p = str(x[1])

        if m[0] != '%':     # not a valid macro so just skip it
            continue

        if '%' in p:
            b = True

        text = text.replace(m, p)

    if b and save != text:
        patch(text, patches)

    return text


def default_patches():
    p = [
        ["%date", datetime.datetime.now().strftime("%x")],
        ["%time", datetime.datetime.now().strftime("%X")],


        ]
    return p