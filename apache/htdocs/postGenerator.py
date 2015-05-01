
import htmlPatcher
import os

#max 24 posts per page 


def genPicPost(x, y, image):
	p = [["%x", x], ["%y",y], ["%img", image]]
	return htmlPatcher.patchPage("imgPost.t", p)

def genTextPost(x, y, text):
	p = [["%x", x], ["%y",y], ["%textPost", text]]
	return htmlPatcher.patchPage("textPost.t", p)

def genMain(circleDir):
	m = ""

	import glob
	l = glob.glob(circleDir + "*")
	file_date_tuple_list = [(x,os.path.getmtime(x)) for x in l]
	file_date_tuple_list.sort(key=lambda x: x[1])
	file_date_tuple_list.reverse()
	l = [x[0] for x in file_date_tuple_list]
 
	i = 0
	for y in range(0,6): 
		for x in range(0,4):  
			id = y*4 + x
			if id >= len(l): return m
			XX = x*322
			YY = y*322
			t = l[id] 
			if t.endswith(".txt"):
				m += genTextPost(XX, YY, open(t).read())
			elif t.endswith(".jpg") or t.endswith(".png") or t.endswith(".gif"):
				m += genPicPost(XX, YY, t)
	return m

#print(genMain("circles\\" + str(0) + "\\"))