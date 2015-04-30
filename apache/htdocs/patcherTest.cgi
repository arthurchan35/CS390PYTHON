#!/usr/bin/python

import htmlPatcher
import datetime
s = "Content-type: text/html\n\n"


print(htmlPatcher.patch_html("test.t", [["%date", datetime.datetime.now()]]))
