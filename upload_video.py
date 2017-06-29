#!/usr/bin/python
import cgi, os
import datetime
import time
from datetime import date
import cassandra
import cgitb; cgitb.enable()
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
#get value from form webpage
form = cgi.FieldStorage()
name = form.getvalue("name")
description = form.getvalue('description')
category= form.getvalue('category')
#v_id=1
views=0
upload_date=datetime.datetime.now()
v_date = date.today()


#upload_date= p
#upload_date = {}
#upload_date['last_sent'] = datetime.datetime.now()
# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('videos/' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'

link='/videos/'+fn
#connection to cassandra database started:
cluster = Cluster()
session = cluster.connect('smg_space')
result = session.execute("select * from sendmygift_videos")
r = session.execute("SELECT MAX(v_id) AS id FROM sendmygift_videos")
v_id = r[0].id + 1
stmt = session.prepare("INSERT INTO sendmygift_Videos (category,name,description,link,upload_date,v_id,views,v_date) VALUES (?, ?, ?, ?, ?, ?, ?, ? )")
batch = BatchStatement()
batch.add(stmt, [category,name,description,link,upload_date,v_id,views,v_date])
session.execute(batch)
result=session.execute("select * from sendmygift_Videos")

# creation of thumbnail started from there for uploaded video file
for root, dirnames, filenames in os.walk('/var/www/html/cgi-bin/Demo++/videos/'):
  for filename in filenames:
    if filename.lower().endswith(('.m4v', '.mov', '.mpeg', 'mp4')): 
      ifile = os.path.join(root, filename)
      ofile = os.path.splitext(ifile)[0] + ".png"
      try:
        with open(ofile) as f: pass
      except IOError as e:
        print "Generating thumbnail for: " + ifile
# print "fftoption of thumbnail start" 
        fftoptions = "-s0 -f"
        command = "ffmpegthumbnailer -i %s -o %s %s" % (ifile, ofile, fftoptions)
 
        p = os.popen(command,"r")
        while 1:
          line = p.readline()
          if not line: break
          print line
#display on webpage started from there:
#import sys
#sys.stdout = open("/var/www/html/cgi-bin", "w")
#print ("test sys.stdout")
#print "Location:index2.py\r\n"
print "Content-type:text/html\r\n\r\n"
#print "Location:/var/www/html/cgi-bin/index2.py"
#import sys
#sys.stdout = open("c:\\goat.txt", "w")
#print ("test sys.stdout")

print "<!DOCTYPE html>"
print "<html>"
print "<head>"
#print "<style>"
#print '<link rel="stylesheet" type="text/css" href="style.css">'
#print ".outer{ width:100%; display:block;}"

#print ".v-container { width:250px; height: 150px; display:inline-block; } "           
#print "</style>" 
print "<title>Demo++</title>"
print "</head>"
print "<body>"
#print "<a href='index2.py'></a>"


#upload video button
#print '<form action="upload.html" method="post">'

#print '<input type="submit" value=" upload videos">'
#print '</form>'
#print "<h1>sendmygift</h1>"

#print '<form enctype="multipart/form-data"' 
#print 'action="index2.py" method="post">'
#print '</form>'
#print "<div class='outer'>"
#print "<div class='inner'>"

#for r in result:
#	link = r.link
#        start= link.find('/videos/')+8
#        end = link.find('.')
#        vname = link[start:end]

 #       print "<a href='test_video.py?vname="+vname+"'>"
 #       print "<div class='v-container'>"
 #       print '<div class="video">'


  #      print '<video preload="metadata" width="200" height="200" poster="/videos/'+vname+'.jpg" >'
   #     print '<source src="'+r.link+'" type="video/mp4">'
   #     print '<source src="'+r.link+'" type="video/webm">'
   #     print '<source src="'+r.link+'" type="video/ogg">'
   #     print '<source src="'+r.link+'" type="video/wmv">'
   #     print "</video>"
    #    print "<div class='name-desc'>"
    #    print "<h2 class='title'>"
    #    print r.name
    #    print "</h2> <p class='desc'>"
   #     print r.description
   #     print "</p></div>"
   #     print "</a>"





#	print "</div>"
#        print "</div>"
#
#print "</div>"
#print "</div>"
print "<h2 >File Uploaded Sucessfully CLICK Backspace to Upload more File </h2>  "
print "</body>"
print "</html>"


