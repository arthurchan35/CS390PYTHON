#!/usr/bin/python

import htmlPatcher
import currentuser

print('Set-Cookie: userid=2134')

print("Content-type: text/html\n\n")

p  = htmlPatcher.default_patches()  # set of common patches

p += currentuser.currentUserInfo()	# user info




print(htmlPatcher.patchPage("base.t", p))



