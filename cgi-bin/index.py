#!/usr/bin/python
#coding=utf-8

import os

print("Content-type: text/html\r\n\r\n")
print("<meta charset=\"utf-8\">")
print("<b>Enviroment</b></br>")
print("<ul>")
for param in os.environ.keys():
	print("<li><span style='color:green'>%20s</span>: %s</br></li>"%(param, os.environ[param]))
print("</ul>")
print("<html>")
print("<head>")
print("<title> title </title>")
print("</head>")
print("<body>")
print("<h2> hello this is the first page</h2>")
print("</body>")
print("</html>")
