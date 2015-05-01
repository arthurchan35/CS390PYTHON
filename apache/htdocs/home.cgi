#!/usr/bin/python

import htmlPatcher
import currentuser
import os
import Cookie

print('Set-Cookie: userid=2134')
print("Content-type: text/html\n\n")
cookie_string = os.environ.get('HTTP_COOKIE')
C = Cookie.SimpleCookie()
C.load(cookie_string)
uid = C["userid"].value


p  = htmlPatcher.default_patches()  # set of common patches
p += currentuser.currentUserInfo()	# user info
p += [["%cookiestring", cookie_string], ["%userid", uid]]



print(htmlPatcher.patchPage("base.t", p))



