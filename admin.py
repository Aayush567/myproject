#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
#from requests import Request, Session

#from mod_python import Session
#from cassandra.cluster import Cluster
#from cassandra.query import BatchStatement
#get value from form webpage
form = cgi.FieldStorage()
user_id = form.getvalue("user_id")
password = form.getvalue('password')
#session = Session.Session(req)
#s = requests.Session()

if ( user_id == 'smg' and password == 'smg@123'):
	#s.get('http://localhost/cookies/set/islogin/1')
	print "Location:category1.py\r\n"
	
else:
	t = 'Please enter correct password! & user-id!'	
	

#res = s.get('http://localhost/cookies')

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Site - Status</title>"
print "</head>"
print "<body>"
#print "session status:"
#print res.text
print "<h2> %s </h2>" % t
print "</body>"
print "</html>"

