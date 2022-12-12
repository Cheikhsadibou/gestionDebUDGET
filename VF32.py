""" 
======> pour l'afficher sous form d'une ligne :

import sqlite3
 
connection = sqlite3.connect("GestionDBudget.db")
cursor = connection.cursor()

req = cursor.execute('SELECT * FROM GestionDeBudget')

for row in req.fetchall():

       print(row)

connection.close()

======>pour afficher les donner saisis : 

import sqlite3
 
connection = sqlite3.connect("GestionDBudget.db")
cursor = connection.cursor()
req = cursor.execute('SELECT * FROM GestionDeBudget')
print(req.fetchall)
connection.close()

======>  pour inserer une  donner dans le tableau :

import sqlite3
 
connection = sqlite3.connect("GestionDBudget.db")
cursor = connection.cursor()

new_user = (cursor.lastrowid, "TYPE_DE_REVENUE", "type_de_revenue")

cursor.execute('INSERT INTO GestionDeBudget VALUES(?,?,?)', new_user)
connection.commit()

print("De nouvelle donner sont ajouter !!!")

connection.close()         
                                          
"""
import sqlite3
 
connection = sqlite3.connect("GestionDBudget.db")
cursor = connection.cursor()

req = cursor.execute('SELECT * FROM GestionDeBudget')

for row in req.fetchall():

       print(row)

connection.close()
