#!/usr/bin/python

import htmlPatcher
import currentuser


print("Content-type: text/html\n\n")

p  = htmlPatcher.default_patches()  # set of common patches
p += htmlPatcher.templates()
p += currentuser.currentUserInfo()	# user info




print(htmlPatcher.patchPage("base.t", p))



