#!/usr/bin/python
import cgi, cgitb
from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('smg_space')
result = session.execute(" select * from category ")


print "Content-type:text/html\r\n\r\n"




print "<!DOCTYPE html>"
print "<html>"
print '<head>'
#print '<style>'
print '<link rel="stylesheet" type="text/css" href="style1.css">'
print '<title>test</title>'
#print "</style>"
print "</head>"
print "<body>"


print '<div class="container">'

print '<header>'
print '<h1>Dashboard</h1>'
print '</header>'
 
print '<nav>'
print '<ul>'
print '<li color:red><a href="category1.py">Menu</a></li>'
print '<li><a href="upload_videos5.py">Add Category</a></li>'
print '<li><a href="add_category2.py">Upload Videos</a></li>'
print '<li><a href="index.py">Log-Out </a></li>'
print '</ul>'
print '</nav>'

print '<article>'
#print '<h1> </h1>'
#print '<p></p>'
print '<div class="outer">'
print '<form action="add_category1.py" method="post">'
print 'ADD CATEGORY : <br> <input type="text" name="category" required="required" /> <br/>'
print '<p><input type="submit" value="Add-category" /></p>'
print '</form>'
print '</div>'
print '</article>'

print '<footer>Copyright (c) Sendmygift.com</footer>'

print '</div>'

print '</body>'
print '</html>'

