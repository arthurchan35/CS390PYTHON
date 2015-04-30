#!/usr/bin/python

import subprocess
import os

s = """Content-type: text/html

<H1>Updating Server From Git...</H1>
"""
print(s)

subprocess.call("chmod +x ./../../restartServer.sh", shell=True)
subprocess.call("./../../restartServer.sh", shell=True)