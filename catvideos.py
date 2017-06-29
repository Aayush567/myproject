#!/usr/bin/python
import cgi,os
import cgitb;cgitb.enable()
from urllib2 import Request, urlopen, URLError
form = cgi.FieldStorage() 
cat = form.getvalue('cname')

from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('smg_space')
result = session.execute(" select * from sendmygift_Videos WHERE category ='"+cat+"'")
q = session.execute(" select * from category ")


print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print '<link rel="stylesheet" type="text/css" href="style.css">'
print "<title>Demo++</title>"
print "<style>"
print "</style>"
print "</head>"
print "<body>"
print '<header class="headre-space">'
print "<div class=' header'>"
print "<div class='logo'>"
print "<h1>Demo++</h1>"
print "</div>"
print "<div class='search'>"
print '<form>'
print '<input type="text" name="search" placeholder="Search..">'
print '</form>'
print '</div>'
print '<div class="upload">'

print '</div>'
print '</div>'
print '</header>'

#print cat
print "<div class='outer'>"
print "<div class='inner'>"
print '<div class="side-var">'
print '<ul>'
print ' <li><a class="active" href="index.py">Home</a></li>'
print ' <li><a href="admin.html">Upload Videos</a></li>'
for t in q:
	l=t.category
	print ' <li><a href="catvideos.py?cname='+l+'">'
        print t.category
        print '</a></li>'
print '</ul>'
print '</div>'        
print '<div class="video">'
for r in result:
        
        print "<div class='v-container'>"
	link = r.link
	start= link.find('/videos/')+8
	end = link.find('.')
	vname = link[start:end]
        print "<a href='test_video.py?vname="+vname+"'>"

         
        print '<video preload="metadata" width="200" height="100" poster="/videos/'+vname+'.jpg" >'
                                
       
        print '<source src="'+r.link+'" type="video/mp4">'
        print '<source src="'+r.link+'" type="video/webm">'
        print '<source src="'+r.link+'" type="video/ogg">'
        print '<source src="'+r.link+'" type="video/wmv">'                
        print "</video>"
	

        print "<div class='name-desc'>"
        print "<ul><li>"           
        print r.name
        print "</li> <li><span>"
        print r.description
        print "</span></li></ul></div>"
        print "</a>"
	print "</div>"
print "</div>"
print "</div>"
print '<footer>'
print '<p>Copyright 2016 (c) Demo++ </p>'
print '</footer>'
print "</body>"
print "</html>"


 
