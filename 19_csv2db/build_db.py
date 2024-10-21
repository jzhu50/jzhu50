#Boas: Michelle Zhu, Ryan Zhou, Linda Zheng
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#10/20/2024
#time spent: 1

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="00.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

#c.execute("CREATE TABLE roster (name TEXT, age INTERGER, id INTEGER)")

with open('students.csv', mode='r', newline='') as file:
    csv_reader = csv.DictReader(file) #reads csv file as an ordered dictionary
    for row in csv_reader:
        #print(row)
        name = (row['name'])
        age = (row['age'])
        id = (row['id'])
        command = "INSERT INTO roster (name, age, id) VALUES (?, ?, ?)" # test SQL stmt in sqlite3 shell, save as string
        c.execute(command, (name, age, id))    # run SQL statement
#table = c.execute("select * from roster")
#print(table)
#==========================================================

db.commit() #save changes
db.close()  #close database
