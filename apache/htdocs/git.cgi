#!/usr/bin/python

import subprocess
import os

s = """Content-type: text/html

<H1>Updating Server From Git...</H1>
"""
print(s)

subprocess.call("chmod +x ./../../resetServer.sh", shell=True)
#subprocess.call("./../../resetServer.sh", shell=True)
subprocess.Popen("nohup ./../../resetServer.sh", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)