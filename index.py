#!/usr/bin/python
import cgi, cgitb
import time
from datetime import date
today= date.today()
from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('smg_space')
result = session.execute(" select * from sendmygift_Videos  ")
q = session.execute(" select * from category  ")
#import time
#from datetime import date
today = date.today()
#print today
#now=date.today()
#days=(now-today)
#print days
print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print '<link rel="stylesheet" type="text/css" href="style.css">'
print "<title>Demo++</title>"
print "<style>"
print "</style>"
print "</head>"
print '<body>'
print '<header class="headre-space">'
#print "<div class=' header'>"
print "<div class='logo'>"
print "<h1>Demo++</h1>"
print "</div>"
print "<div class='search'>"
print '<form action="search.py" method="post">'
print '<input type="text" name="search" placeholder="Search..">'
#print '<input type="submit" value="search">'
print '</form>'
print '</div>'
print '<div class="upload">'
#print '<form action="admin.html">'
print '<form class="upload1" action="admin.html" method="post">'
print '<input type="submit" value=" upload">'
print '</form>'
print '</div>'
print '</div>'
print '</header>'
print "<div class='outer'>"
print "<div class='inner'>"
print '<div class="side-var" color="white">'
print '<ul>'
print ' <li><a class="active" href="index.py">Home</a></li>'
print ' <li><a href="admin.html">Upload Videos</a></li>'
for t in q:
       # print ' <li><a href="music.py?vname='+vname+'">'
        l=t.category 
        print '<li><a href="catvideos.py?cname='+l+'">'
	print t.category
	print ' </a></li>'
print '</ul>'
print '</div>'
print '<div class="video">'
for r in result:
        
        print "<div class='v-container'>"
 
        t=r.upload_date
#    	t=a,b,c,d,e,f,g
#	start=t.find('22  ') 
#	end=t.find('.')
#        q=t[start:end]      
	link = r.link
	start= link.find('/videos/')+8
	end = link.find('.')
	vname = link[start:end]
        p=str(r.v_id)
        print "<a href='test_video.py?vname="+vname+"& v_id="+p+"'>"
        print '<video preload="metadata" width="200" height="100" poster="/videos/'+vname+'.jpg" >'
        print '<source src="'+r.link+'" type="video/mp4">'
        print '<source src="'+r.link+'" type="video/webm">'
        print '<source src="'+r.link+'" type="video/ogg">'
        print '<source src="'+r.link+'" type="video/wmv">'                
        print "</video>"
	print "<div class='name-desc'>"
        print "<ul><li>"           
        print r.name
        print "</li><li>"
        print "<span>"
	print r.description
        print "</span>"
	print "<br>"
	print "<span class='upload_date'>"
#	print days
	print "upload:"
#	x=r.v_date
#        y=(today-x)
	print r.v_date
#	print "<br>"
	#print r.views
	print "</span></li><li>" 
	print "</li> </ul></div>"
        print "</a>"
	print "</div>"
print "</div>"
print "</div>"
print '<footer>'
print '<p>Copyright 2016 (c) Demo++ </p>'
print '</footer>'
print "</body>"
print "</html>"


 
