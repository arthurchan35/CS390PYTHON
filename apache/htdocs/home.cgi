#!/usr/bin/python

import htmlPatcher
import currentuser
import os

print('Set-Cookie: userid=2134')
print("Content-type: text/html\n\n")
cookie_string = os.environ.get('HTTP_COOKIE')


p  = htmlPatcher.default_patches()  # set of common patches
p += currentuser.currentUserInfo()	# user info
p += [["%cookiestring", cookie_string]]



print(htmlPatcher.patchPage("base.t", p))



