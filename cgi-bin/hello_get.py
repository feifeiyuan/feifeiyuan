#!/usr/bin/python
#coding=utf-8
import cgi
import cgitb
print("Content-type: text/html\r\n\r\n")
form = cgi.FieldStorage()
site_name = form.getvalue('name')
site_url = form.getvalue('url')
site_youj = form.getvalue('youj')
site_google = form.getvalue('google')
site_radio = form.getvalue('site')
site_text = form.getvalue('text')
site_select = form.getvalue('dropdown')
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>feifei</title>")
print("</head>")
print("<body>")
if site_name and site_url:
	print("<p>%s:%s</p></br>"%(site_name, site_url))
if site_youj and site_google:
	print("<h2>%s:%s</h2></br>"%(site_youj, site_google))
if site_radio:
	print("<p>%s</p>\n"%(site_radio))
if site_text:
	print("<p>%s</p>\n"%(site_text))
if site_select:
	print("<p>%s</p>\n"%(site_select))
print("</body>")
print("</html>")
