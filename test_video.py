#!/usr/bin/python
import cgi
import cgitb;cgitb.enable()
from urllib2 import Request, urlopen, URLError
form = cgi.FieldStorage() 
a=form.getvalue('vname')
vid=form.getvalue('v_id')

from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect('smg_space')
q = session.execute(" select * from category  ")
result = session.execute(" select * from sendmygift_Videos  ")
print "Content-type:text/html\r\n\r\n"
print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print '<link rel="stylesheet" type="text/css" href="style5.css"/>'
print "<title>Demo++</title>"
print '<style type="text/css">'
print "</style>"
print "<script src='jquery.js'></script>"

print "<script src='javascript.js'></script>"
print "<script>setTimeout(function(){$('.video-add').remove();}, 7000); </script>"

print "<script type='text/javascript'>"
#print "<script>setTimeout(function(){$('.video-add').remove();}, 5000); </script>"
print "$(document).ready(function() {$('video').videoPlayer({'playerWidth' : 0.95,'videoClass' : 'video'});});"

print "</script>"
print "</head>"
print "<body>"
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
#print '</div>'
print '</header>'
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
#print "<div>"
#print '<h2><a class="active" href="index.py">Home</h2></a>'
#print '</div>'
print '<div class="container">'
#print '<div class="advertise">'

#print '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'
#print '<!-- 336*280 -->'
#print '<ins class="adsbygoogle"style="display:inline-block;width:336px;height:280px"data-ad-client="ca-pub-7660213401140271"data-ad-slot="1132178542"></ins>'
#print '<script>'
#print '(adsbygoogle = window.adsbygoogle || []).push({});'
#print '</script>'

print '<video width="700" height="400">'
print '<source src="/videos/'+a+'.mp4" type="video/mp4">'

#print a
print '<source src="/videos/'+a+'.webm" type="video/webm">'
print '<source src="/videos/'+a+'.ogg" type="video/ogg">'
print '<source src="/videos/'+a+'.ogg" type="video/mpg">'
#print '<div class="advertise">'

#print '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'
#print '<!-- 336*280 -->'
#print '<ins class="adsbygoogle"style="display:inline-block;width:336px;height:280px"data-ad-client="ca-pub-7660213401140271"data-ad-slot="1132178542"></ins>'
#print '<script>'
#print '(adsbygoogle = window.adsbygoogle || []).push({});'
#print '</script>'
  
print '</video>'

print '<div class="video-add">'
print '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'
print '<!-- 336*280 -->'
print '<ins class="adsbygoogle"style="display:inline-block;width:336px;height:280px"data-ad-client="ca-pub-7660213401140271"data-ad-slot="1132178542"></ins>'
print '<script>'
print '(adsbygoogle = window.adsbygoogle || []).push({});'
print '</script>'
print '</div>'

print '<div class="videos-block">'
for r in result:
        
        print "<div class='v-container'>"

        
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
	print "<span class='upload-date'>"
	print r.v_date
#	print "<br>"
#	print r.p
	print "</span></li><li>" 
	print "</li> </ul></div>"
        print "</a>"
	print '</div>'
print '</div>'
print '<div class="advertise">'

print '<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>'
print '<!-- 336*280 -->'
print '<ins class="adsbygoogle"style="display:inline-block;width:336px;height:280px"data-ad-client="ca-pub-7660213401140271"data-ad-slot="1132178542"></ins>'
print '<script>'
print '(adsbygoogle = window.adsbygoogle || []).push({});'
print '</script>'
print '</div>'

print '</div>'
print '<footer>'
print vid 
print '<p>Copyright 2016 (c) Demo++ </p>'
print '</footer>'
print '</body>'

print '</html>'
