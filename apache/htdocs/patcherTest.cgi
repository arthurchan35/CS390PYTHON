#!/usr/bin/python

import htmlPatcher
import datetime

print(htmlPatcher.patch_html("test.t", [["%date", datetime.datetime.now()]]))
