#!/usr/bin/python

import htmlPatcher
import currentuser
import os
import http.cookies

print('Set-Cookie: userid=2134')
print("Content-type: text/html\n\n")
cookie_string = os.environ.get('HTTP_COOKIE')


p  = htmlPatcher.default_patches()  # set of common patches
p += currentuser.currentUserInfo()	# user info
p += [["%cookiestring", cookie_string]]

#C = http.cookies.SimpleCookie()
#C.load(cookie_string)
#p += [["%userid", C["userid"] ]]


print(htmlPatcher.patchPage("base.t", p))



