"Mise en plce d'une plateforeme de getion de budget"

#inmportation de libra
from tinydb import TinyDB, Query
from datetime import date


# creer une liste de menu
SERVEUR_USER = ""

ENREGISTER_DEPENSE = ""

ENREGISTER_REVENUE = ""

MONTANT = ""

ECART_TYPE = ""

TYPE_DE_REVENUE = ""

TYPE_DEPENSE = ""

DATE = ""



# créer une fonction pour ajouter l'express aux listes et organiser les donnée

db = TinyDB("user_db.json")


def add_Express(serveur_user, Enregistrer_depense, Enregistrer_revenue, Montnat, Ecart_type, type_de_revenue,dépense_type, date):

  item = {
    'SERVEUR_USER': serveur_user, 
    'ENREGISTER_DEPENSE': Enregistrer_depense,
    'ENREGISTER_REVENUE':Enregistrer_revenue,
    'MONTANT':Montnat,
    'ECART_TYPE':Ecart_type,
    'TYPE_DE_REVENUE':type_de_revenue,
    'TYPE_DEPENSE': dépense_type,
    'DATE' :date,
     }


  db.insert({'nom': item})
 
  
add_Express('serveur_user', 'Enregistrer_depense', 'Enregistrer_revenue', 'Montnat', 'Ecart_type', 'type_de_revenue', 'dépense_type', 'date')
# menue du programme 

option = 1 # ce sera l'option ou le choix ou l'entrée des utilisateur 

while( option !=0):
  #create the fonction menu

  print(" bienvenue dans le Menu des suivis de Gestion de budget ")
  print(" 1. Ajouter des dépenses ")
  print(" 2. Enregistrer un nouveau revenue ")
  print(" 3. Ajouter un nouveau versement ")
  print(" 4. Afficher les rapports des dépenses et revenues")
  print(" 5. Afficher l'écart qui est entre les dépenses et les revenus")
  print(" 0. Exit ")
  option = int(input("Choisis une option:\n "))
  
  # Ajout d'une nouvelle ligne 
 

# Vérifiez le choix ou l'option ou l'entrée de l'utilisateur
  if option == 0 :
    print("sortie du programme")
    break
  elif option == 1:
    print("Ajout de depenses ")
    TYPE_DEPENSE = "Food"
  elif option == 2:
    print("Ajout de nouveau revenue")
    TYPE_DEPENSE == "business"
  elif option == 3:
    print("Ajout d'une nouveau versement")
    TYPE_DEPENSE == "versement"
  elif option == 4:
    print("Affiche du raport des depenses ")
    TYPE_DEPENSE == "versement"
  elif option == 5:
    print("Affichage du Ecart entre les depenses et revenus ")
    ECART_TYPE == 6

  elif option == 7 :
  # créer une base de données et ajouter les dépenses
    db = {
    'SERVEUR_USER': 'serveur_user', 
    'ENREGISTER_DEPENSE': 'Enregistrer_depense',
    'ENREGISTER_REVENUE':'Enregistrer_revenue',
    'MONTANT':'Montnat',
    'ECART_TYPE':'Ecart_type',
    'TYPE_DE_REVENUE':'type_de_revenue',
    'TYPE_DEPENSE': 'dépense_type',
    'DATE' :'date',
    }
  # save the expence raport 
    db.count("user_db.json" == 'serveur_user')
  # show the expence raport 
  print(db)
else:
  print("vous avez choisissez une mauvaise option. Choisissez s'il vous plaît 0, 1, 2, 3, 4 or 5 ")
  # Permettre à l'utilisateur d'entrer le service 

if option == 1 or option == 2 or option == 3 or option == 4 or option == 5:
    serveur_user = input("entrez le service pour le type de dépense " +TYPE_DEPENSE+ ":\n" )
    Montnat = float(input("Entrez le prix  du service :\n"))
    today = date.today
    ENREGISTRER_REVENUE =float(input(serveur_user, Montnat, today,TYPE_DEPENSE))
# Afficher une nouvelle ligne
print()