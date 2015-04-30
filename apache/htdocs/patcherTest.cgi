#!/usr/bin/python

import htmlPatcher
import datetime

print("Content-type: text/html\n\n")

p = htmlPatcher.default_patches()  # set of common patches
print(htmlPatcher.patch_html("test.t", p))
