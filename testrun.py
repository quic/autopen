#!/usr/bin/python
import MySQLdb
#import peewee
#from peewee import *
db = MySQLdb.connect(host="autopen.c5eqmploekdx.us-east-2.rds.amazonaws.com", user="SHIFT", passwd="%&12SHilaE7", db="autopen", port=3306)
cursor = db.cursor();
#valueSend = "INSERT INTO Cars (Model,ModelYear) VALUES ('tiotott','1998');"
#cursor.execute(valueSend)
cursor.execute("SELECT * FROM Exploits");
numrows = cursor.rowcount
cars = cursor.fetchall()

for V in cars:
	print V[2]
#v= 'Toyotaw'
#if v in cars[0]:
#	print 'Yes'
#else:
#	print 'no'
#for row in cars:
	#print row[0],row[1],row[2]
#row = cursor.fetchone()
#print row
#for x in range(0, numrows):
#	row = cursor.fetchone()
#	print row[0], "-->", row[1]
#db.close()
db = MySQLdb.connect(host="autopen.c5eqmploekdx.us-east-2.rds.amazonaws.com", user="SHIFT", passwd="%&12SHilaE7", db="autopen", port=3306)
cursor = db.cursor();

cursor.execute("SELECT * FROM Cars");
numrows = cursor.rowcount
cars = cursor.fetchall()
cursor.execute("SELECT * FROM Exploits");
exploits = cursor.fetchall()
db.close()
x = .1
y = .9
for row in cars:
	#x = x + z
	myString = "<CarsPage>:\n\tButton:\n\t\tid:"+str(row[1])+"\n\t\ttext: '" + str(row[1]) + "'\n\t\tsize_hint: .25, .1\n\t\tpos_hint: {'x':" + str(x) + ", 'y':" + str(y)+"}"
	parttwo = "\n\t\ton_press:\n\t\t\troot.manager.transition.direction='left'\n"
	partthree= "\t\t\troot.manager.transition.duration=.5\n\t\t\troot.manager.current='carinfo'"
	y -= .1
        partfour = "\n\t\ton_press:\n\t\t\troot.manager.get_screen('carinfo').work('"+ str(row[1])+"')"
	#parttwo = "\n\t\ton_press:\n\t\t\troot.cars("+str(row[0])+")"
	Builder.load_string(myString+parttwo+partthree+partfour)
	myString = ''
