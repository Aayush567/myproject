#!/usr/bin/python
import cgi, cgitb
form = cgi.FieldStorage()
p = form.getvalue('category')
category=p.upper()
from cassandra.cluster import Cluster
from cassandra.query import BatchStatement
cluster = Cluster()
session = cluster.connect('smg_space')
result = session.execute("select * from category")
r = session.execute("SELECT MAX(s_no) AS sno FROM category")

#exist=0
for t in result:
	if(t.category == category ):
		exist=1
                break
	else:
		exist=0
	
if(exist==0):
	s_no = r[0].sno + 1
	stmt = session.prepare("INSERT INTO category (s_no, category) VALUES (?, ?)")
	batch = BatchStatement()
	batch.add(stmt, [s_no, category])
	# execute the batch
	session.execute(batch)
	message="category added sucessfully"
else:
	message="category already exit in list"
        
result=session.execute("select * from category")

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Category_List</title>"
print "</head>"
print "<body>"
#print category
print "<h1>"+ message +"</h1>"
#print exist
print "<table class='data' border=1>"
print "<tr> <th> category </th>" 
for r in result:
        print "<tr><td>"
	print r.category
        print "</td></tr>"
      
print "</table>"
print "</body>"
print "</html>"
