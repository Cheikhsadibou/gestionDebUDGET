"Mise en plce d'une plateforeme de getion de budget"

#inmportation de libra
import sqlite3
from datetime import date

# creer une liste de menu

SERVEUR_USER                   = ""
ENREGISTER_DEPENSE             = ""
ENREGISTRER_REVENUE            = ""

MONTANT                        = ""
ECART_TYPE                     = ""

TYPE_DE_REVENUE                = ""
TYPE_DEPENSE                   = ""
DATE                           = ""

# créer une fonction pour ajouter l'express aux listes et organiser les donnée

def add_Express(serveur_user, Enregistrer_depense, Enregistrer_revenue, Montnat, Ecart_type, type_de_revenue,dépense_type, date):
  SERVEUR_USER.append(serveur_user)
  ENREGISTER_DEPENSE.append(Enregistrer_depense)
  ENREGISTRER_REVENUE.append(Enregistrer_revenue)
  MONTANT.append(Montnat)
  ECART_TYPE.append(Ecart_type)
  TYPE_DE_REVENUE.append(type_de_revenue)
  TYPE_DEPENSE.append(dépense_type)
  DATE.append(date)

# menue du programme 

option = 1 # ce sera l'option ou le choix ou l'entrée des utilisateur 

while( option !=0):
  #create the fonction menu

  print("Application de Gestion de Budget avec Python et Sqlite3")
  print("")

  print(" bienvenue dans le Menu des suivis de Gestion de budget ")
  print(" 1. Ajouter des dépenses ")
  print(" 2. Enregistrer un nouveau revenue ")
  print(" 3. Ajouter un nouveau versement ")
  print(" 4. Afficher les rapports des dépenses et revenues")
  print(" 5. Afficher l'écart qui est entre les dépenses et les revenus")
  print(" 0. Exit ")

  option = int(input("Choisis une option:\n "))
  
  # Ajout d'une nouvelle ligne 
print("")

# Vérifiez le choix ou l'option ou l'entrée de l'utilisateur
while option == 0 :
  break
if option == 1:
  print("Ajout de depenses ")
  TYPE_DEPENSE = "Food"
elif option == 2:
  print("Ajout de nouveau revenue")
  TYPE_DEPENSE == "business"
elif option == 3:
  print("Ajout d'une nouveau versement")
  TYPE_DEPENSE == "revenu"
elif option == 4:
  print("Affiche du raport des depenses ")
  TYPE_DEPENSE == "versement"
elif option == 5:
  print("Affichage du Ecart entre les depenses et revenus ")
  ECART_TYPE == 6

elif option == 7 :
  # créer une base de données et ajouter les dépenses
  with sqlite3.connect("Gestion.db") as connection:
    cursor = connection.cursor()


    cursor.execute(
  'CREATE TABLE contacte (id INTEGER PRIMARY KEY AUTOINCREMENT,'
  db{'serveur_user'} = SERVEUR_USER:
  db{'Enregistrer_depense'} = ENREGISTER_DEPENSE:
  db{'Enregistrer_revenue'} = ENREGISTRER_REVENUE:
  db{'Montnat'} = MONTANT:
  db{'Ecart_type'}  = ECART_TYPE:
  db{'type_de_revenue'} = TYPE_DE_REVENUE:
  db{'date'} = DATE

  )
    
    
  # save the expence raport 
  connection.commit()
  # show the expence raport 
  print(cursor.execute)
else:
  print("you choose an incorrect option. plaese choose 0, 1, 2, 3, 4 or 5 ")
  # Allow the user to enter the good or service and the pry 

if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
    serveur_user = input("enter the good or service for the expense type " +TYPE_DEPENSE+ ":\n" )
    Montnat = float(input("Enter the price of the good or service :\n"))
    today = date.today
    ENREGISTRER_REVENUE(serveur_user, Montnat, today,TYPE_DEPENSE)
# print a new line
print()