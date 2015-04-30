#!/usr/bin/python

import subprocess
import os

s = """Content-type: text/html

<H1>Updating Server From Git...</H1>
"""
print(s)

subprocess.call("/../../git fetch --all")
subprocess.call("/../../git reset --hard origin/master")
subprocess.call("/../../chmod -R +x apache")
subprocess.call("/../../apache/bin/apachectl restart")

