#!/usr/bin/python

import htmlPatcher
import currentuser
import os
import Cookie
import postGenerator


def homeGen():

	print("Content-type: text/html\n\n")
	#cookie_string = os.environ.get('HTTP_COOKIE')
	#C = Cookie.SimpleCookie()
	#C.load(cookie_string)

	#if "userid" not in C:
	#	uid = 1
	#else:
	#	uid = C["userid"].value
	uid = 1
	curr_circle = 0

	p  = htmlPatcher.default_patches()  # set of common patches
	p += currentuser.currentUserInfo(1)	# user info
	p += [["%userid", uid]]
	p += [["%posts", postGenerator.genMain("circles\\" + str(curr_circle) + "\\")]]


	print(htmlPatcher.patchPage("base.t", p))

homeGen()