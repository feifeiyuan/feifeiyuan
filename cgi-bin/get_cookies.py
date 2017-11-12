#!/usr/bin/python
#coding=utf-8
import os
import Cookie

print("Content-type: text/html\r\n\r\n")

#print("cookie : %s"%(os.environ['HTTP_COOKIE']))
if 'HTTP_COOKIE' in os.environ:
	cookie_str = os.environ.get('HTTP_COOKIE')#name="w3cschool"
	print(cookie_str)
	print("</br>")
	c = Cookie.SimpleCookie()#cookie对象
	if c:
		print("dgfg")
	c.load(cookie_str)

	print(c)
	print("</br>")
	try:
		data = c['name'].value
		#data = c['name'].value
		print(data)
	except KeyError:
		print("error")
else:
	print("no")
