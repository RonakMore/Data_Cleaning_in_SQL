print("Student Management System")

print("1:Add Student")
print("2:Update Student")
print("3:Delete Student")
print("4:Search Student")

choice=eval(input("Enter Your Choice:"))

import mysql.connector as mysql

conn=mysql.connect(user='root',password='',host='localhost')
cursor=conn.cursor()
q="use project"
cursor.execute(q)
#print("Sucess")


def addstudent():
    a=input("Enter The Student Name:")
    b=input("Enter The Student Marks:")
    c=input("Enter The Student Contact No:")

    q1="insert into student(name,marks,contact) values ('"+a+"','"+b+"','"+c+"')"
    cursor.execute(q1)
    conn.commit()

def updatedata():
    a=input("Enter the Student Id:")
    b=input("Enter The Student Name:")

    u="update student set name='"+b+"' where id='"+a+"'"
    cursor.execute(u)
    conn.commit()

def deletedata():
    a=input("Enter The student Id:")

    d="delete from student where id='"+a+"'"
    cursor.execute(d)
    conn.commit()

def searchdata():
    a=input("Enter The Student Id:")
    q3="select * from student where id='"+a+"'"
    cursor.execute(q3)
    res=cursor.fetchall()
    print(res)

if(choice==1):
    addstudent()
elif(choice==2):
    updatedata()
elif(choice==3):
    deletedata()
elif(choice==4):
    searchdata()






