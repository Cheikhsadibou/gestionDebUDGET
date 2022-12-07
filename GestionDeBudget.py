"Mise en place d'une plateforeme de getion de budget"

#inmportation de libra
import sqlite3 
from datetime import date
import math


# creer une liste de menu
SERVEUR_USER = ""

ENREGISTER_DEPENSE = ""

ENREGISTER_REVENUE = ""

MONTANT = ""
Operation_lancer= True
Montant = str

ECART_TYPE = ""

TYPE_DE_REVENUE = ""

TYPE_DEPENSE = ""
TYPE_DEPENSES = ""

DATE = ""

# créer une fonction pour ajouter l'express aux listes et organiser les donnée

connection = sqlite3.connect("./MonBaseDeDonne/Data_Base.db")
cursor = connection.cursor()


def add_Express(serveur_user, Enregistrer_depense, Enregistrer_revenue, Montant, Ecart_type, type_de_revenue,dépense_type, date):

  item = {
    'SERVEUR_USER': serveur_user, 
    'ENREGISTER_DEPENSE': Enregistrer_depense,
    'ENREGISTER_REVENUE':Enregistrer_revenue,
    'MONTANT':Montant,
    'ECART_TYPE':Ecart_type,
    'TYPE_DE_REVENUE':type_de_revenue,
    'TYPE_DEPENSE': dépense_type,
    'DATE' :date,
     }

 
  
add_Express('serveur_user', 'Enregistrer_depense', 'Enregistrer_revenue', 'Montnat', 'Ecart_type', 'type_de_revenue', 'dépense_type', 'date')
# menue du programme 

option =  1 # ce sera l'option ou le choix ou l'entrée des utilisateur 

while( option !=0):
  #create the fonction menu

  print(" bienvenue dans le Menu des suivis de Gestion de budget ")
  print(" 1. Ajouter des dépenses ")
  print(" 2. Enregistrer un nouveau revenue ")
  print(" 3. Ajouter un nouveau versement ")
  print(" 4. Afficher les rapports des dépenses et revenues")
  print(" 5. Afficher l'écart qui est entre les dépenses et les revenus")
  print(" 0. Exit ")
  try:
    option = int(input("Choisis une option:\n "))
  except ValueError:
    print("\nOption saisis non recommender !\nVeuiller saisir une des principaux options proposer dans le menu !!!\n")
    continue
  else:
    print("Mise en place d'une plateforeme de getion de budget\n")


# Vérifiez le choix ou l'option ou l'entrée de l'utilisateur
  if option == 0:
    print("\tSortie du programme\n\n \tA BIENTOT !!!")
    break

  elif ValueError and option not in (1, 2, 3, 4, 5):
    print("\noption introuvable !!!\n")

  elif option == 1:
    print("Ajout de depenses ")
    serveur_user = input("entrez le service pour le type de dépense\n" )
    Montant = float(input("Entrez le prix  du service  " +serveur_user+ ":\n"))
    today = date.today

    new_user = (cursor.lastrowid, serveur_user , Montant)

    cursor.execute('INSERT INTO GestionDeBudget VALUES(?,?,?)', new_user)
    connection.commit()

    print("De nouvelle donner sont ajouter !!!")

    connection.close() 

  elif option == 2:
    print("Ajout de nouveau revenue")
    business_user = input("Veuiller entrez le  type de ton business " )
    Montnat_business = float(input("Entrez le montant de votre revenue " +business_user+ ":\n"))
    today = date.today

    new_user = (cursor.lastrowid, business_user , Montnat_business)

    cursor.execute('INSERT INTO GestionDeBudget VALUES(?,?,?)', new_user)
    connection.commit()

    print("De nouvelle donner sont ajouter !!!")

    connection.close()

  elif option == 3:
    print("Ajout d'une nouveau versement")
    serveur_user = input("entrez le service pour le type de dépense" )
    Montant = float(input("Entrez le prix  du service " +serveur_user+ ":\n"))
    today = date.today
   
    new_user = (cursor.lastrowid, serveur_user , Montant)

    cursor.execute('INSERT INTO GestionDeBudget VALUES(?,?,?)', new_user)
    connection.commit()

    print("De nouvelle donner sont ajouter !!!")

  elif option == 4:
    print("Affichage du raport des depenses total effectuer !!! \n")

    aff = cursor.execute('SELECT * FROM GestionDeBudget ')
    for row in aff.fetchall():
      print(row)
    

  elif option == 5:
    print("Calcul de  l'Ecart entre les depenses et revenus ")
    while Operation_lancer:
      Montant = input("Entrez la somme depensé :\n")
      try: 
        Montant = int(Montant)
        break
      except:
        print("Option non recomander !!!")

    while Operation_lancer:
      revenu = input("Entrez le revenu effectuer  :\n")
      try:
        revenu = int(revenu)        
        break
      except:
         print("Option non recomander !!!")

    Ecart = Montant - revenu
   

    new_user = (cursor.lastrowid , Montant, revenu, Ecart)

    cursor.execute('INSERT INTO EcartDepenseRevenu2 VALUES(?,?,?,?)', new_user)
    connection.commit()

    text = "\tL'ecart du Depense et du Revenu est  : {} FCFA "
    print(text.format(Ecart))
    print("Ces nouvelles donner de l'Ecart entre Depence et revenu sont ajouter !!!")

  else :
    print("vous avez choisissez une mauvaise option. Choisissez entre  0, 1, 2, 3, 4 or 5 ")
    print("")
    continue
        

connection.close()