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
print("<html>")
print("<head>")
print("<meta charset=\"utf-8\">")
print("<title>feifei</title>")
print("</head>")
print("<body>")
if site_youj and site_google:
	print("<h2>%s:%s</h2>"%(site_youj, site_google))
print("</body>")
print("</html>")
