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
print '<h1> </h1>'
print '<p></p>'
print '</article>'

print '<footer>Copyright (c) Sendmygift.com</footer>'

print '</div>'

print '</body>'
print '</html>'
#print "<!DOCTYPE html>"
#print "<html>"
#print "<title> SendmyGift</title>"
#print "<body>"
#print '<form enctype="multipart/form-data" action="upload_video.py" method="post">'
#print 'SELECT CATEGORY :<br>'
#print '<select name="category">'
#for r in result:
#        print '<option value="'+ r.category +'">'
#        print r.category
#        print '</option>'
#print '</select>'
#print '<br/>'
#print 'NAME        : <br> <input type="text" name="name" required="required"> <br />'
#print 'DESCRIPTION : <br> <input type="text" name="description" required="required" /><br/>'
#print '<p>File: <br> <input type="file" name="filename" /></p>'
#print '<p> <input type="submit" value="Upload" /> </p>'
#print '</form>'
#print '<br>'
#print '<form action="add_category1.py" method="post">'
#print 'ADD CATEGORY : <br> <input type="text" name="category" required="required" /> <br/>'
#print '<p><input type="submit" value="Add-category" /></p>'
#print '</form>'
#print '<form enctype="multipart/form-data" action="admin.html" method="post">'
#print '<p><input type="submit" value="LOG-OUT" /></p>'
#print '</form>'
#print '</body>'
#print '</html>'

