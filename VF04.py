import sqlite3
import math

connection = sqlite3.connect("./MonBaseDeDonne/Data_Base.db")
cursor = connection.cursor()

TYPE_DEPENSE = ""
TYPE_DE_REVENUE = ""

"""
Operateur en python = + (addition)
                      - (soustraction)
                      * (multiplication)
                      / (division)
                      % (modulo) --> reste d'une division Euclidienne 


====> pour calculer la division des nombres et afficher leur resultats :
calcul = 5 / 2
calcul = int(calcul)

calcul1 = 5 % 2
calcul1 = int(calcul1)


print("resultat = ", calcul , "reste", calcul1)


====> pour les variables :
variable = variable + X
variable += X
variable -= X
variable *= X
"""""

# depenses

Montnat = int(input("Entrez la somme depensé :\n"))
revenu = int(input("Entrez la revenu effectuer  :\n"))

Ecart = Montnat - revenu

new_user = (cursor.lastrowid , Montnat, revenu, Ecart)

cursor.execute('INSERT INTO EcartDepenseRevenu VALUES(?,?,?,?)', new_user)
connection.commit()

print("De nouvelle donner de l'Ecart entre Depence et revenu sont ajouter !!!")
