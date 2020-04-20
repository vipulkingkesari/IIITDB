#dbms
import mysql.connector
from mysql.connector import Error
print("this is rough ui of the project ")
mydb=mysql.connector.connect(host='localhost',user='root',passwd='Vipul@kesari1',database='logincredentials')
mycursor=mydb.cursor()
# mycursor.execute("show tables")
# for i in mycursor:
# 	print(i)
sql = "INSERT INTO login (uname,rankp,password) VALUES (%s, %s, %s)"

print("press following")
print("1. for new user")
print("2. for existing user")
a=int(input("press here:"))
if(a==1):
	uname=(input("enter the email id:"))
	rank=(input("enter the rank:"))
	password=(input("enter the password:"))
	apassword=(input("verify password:"))
	val=(uname,rank,password)
	if(password==apassword):
		mycursor.execute(sql,val)
		mydb.commit()


		print("your account has created, run again the program to login!")
	else:
		print("your password verification failed")
elif(a==2):
	logiid=(input("enter the email id:"))
	lpassword=(input("enter the password"))
	#sql="select uname,password from login where uname="+logiid+"and password="+lpassword
	sql="select uname from login where uname=%s"
	unm=(logiid,)
	mycursor.execute(sql,unm)
	result=mycursor.fetchall()
	#k=result.count(logiid)
	#print(k)
	c=0
	for i in result:
		c=c+1

	if(c!=0):
		print("login granted!")
	else:
		print("your login credetials did not match!")

else:
	print("you selected wrong option!")
