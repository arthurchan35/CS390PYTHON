#!/usr/bin/python


def patch_html(file, patches):
    s = open(file).read()

    for x in patches:
        s = s.replace(x[0], str(x[1]))
    return s