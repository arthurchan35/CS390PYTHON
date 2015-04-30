#!/usr/bin/python

import htmlPatcher
import datetime

print("Content-type: text/html\n\n")

print(htmlPatcher.patch_html("test.t", [["%date", datetime.datetime.now()]]))
