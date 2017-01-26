#!/usr/bin/env python

#^ this thing is called the "shebang"
# must be an executable

import os
import json
import cgi
import Cookie

# Leaving this here
#print "Content-Type: text/plain"
#print "Hello world ~*~*~*~*~"
#print json.dumps(dict(os.environ), indent =2, sort_keys = True)


form = cgi.FieldStorage()

username = form.getvalue('user')
password = form.getvalue('password')

C = Cookie.SimpleCookie()
C.load(os.environ['HTTP_COOKIE'])


print "Content-Type: text/html"
if username == "lizard" and password == "hsssss":
	print "Set-Cookie: loggedin=true" 
# ^^ HTTP SYNTAX ^^ and vv we haveHTLM vv 
print 
print "<HTML><BODY>"
print "<H1> ~~~*~~*~~*~*~*~*~*Hello world*~*~*~*~~*~~*~~~ </H1>"
print "Your magic number is:"
print form.getvalue('magic_tracking_number')
print "<P>Your Browser is:"
if "Chrome" in os.environ['HTTP_USER_AGENT']:
	print "Chrome!"
elif "Firefox" in os.environ['HTTP_USER_AGENT']:
	print "Firefox!"


# Make a form
print "<FORM method='POST'><INPUT name='user'><INPUT name='password' type='password'>"
print "<INPUT type='submit'></FORM>"

print "<P>Username: " + str(username)
print "<P>Password: " + str(password)

if username == "lizard" and password == "hsssss":
	print "<P>Login successful!" 

if 'loggedin' in C:
	print "<P>" + str(C['loggedin'].value)
else:
	print "<P>" + "No cookie"






