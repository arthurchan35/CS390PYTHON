#!/usr/bin/python

import htmlPatcher
import currentuser
import os
import Cookie
import postGenerator
import glob

def homeGen():

	print("Content-type: text/html\n\n")
	cookie_string = os.environ.get('HTTP_COOKIE')
	C = Cookie.SimpleCookie()
	C.load(cookie_string)
	
	uid = 0
	if 'userid' in C:
		uid = C['userid'].value
		
		
	curr_circle = 0

	p  = htmlPatcher.default_patches()  # set of common patches
	p += currentuser.currentUserInfo(1)	# user info
	p += [["%userid", uid]]
	p += [["%posts", uid ]]


	print(htmlPatcher.patchPage("base.t", p))

homeGen()