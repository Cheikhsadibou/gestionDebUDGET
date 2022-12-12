"Mise en place d'une plateforeme de getion de budget"

#inmportation de libra
import sqlite3 
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

# créer une fonction pour ajouter l'expression aux listes et organiser les donnée
try:

  with sqlite3.connect("Data_Base.db") as connection:

    cursor = connection.cursor()


  # menue du programme 

  option =  1 # ce sera l'option ou le choix ou l'entrée des utilisateur 

  while( option !=0):
    #create the fonction menu

    print("\nBienvenue dans le Menu des suivis de Gestion de budget de :\t\t \n\tSOKHNA LAYE DIAGNE\n")
    print(" 1. Ajouter des dépenses ")
    print(" 2. Enregistrer un nouveau Revenu ")
    print(" 3. Afficher les rapports des Depenses")
    print(" 4. Afficher les rapports des  Revenues")
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

      with sqlite3.connect("Data_Base.db") as connection:
        cursor = connection.cursor()

      serveur_user = input("entrez le service pour le type de dépense\n" )
      Montant = float(input("Entrez le prix  du service  " +serveur_user+ ":\n"))
      

      new_user = (cursor.lastrowid, serveur_user , Montant)

      # cursor.execute(
      # "CREATE TABLE GestionDeDepenses (id INTEGER PRIMARY KEY AUTOINCREMENT,EntrerUtilisateur TEXT, DonneUtilisateur TEXT)")
      
      cursor.execute('INSERT INTO GestionDeDepense VALUES(?,?,?)',new_user)
      connection.commit()

      print("De nouvelle donner sont ajouter !!!")
      

    elif option == 2:
      print("Ajout de nouveau revenue")

      with sqlite3.connect("Data_Base.db") as connection:
        cursor = connection.cursor()

      business_user = input("Veuiller entrez le  type de ton business\n" )
      Montnat_business = float(input("Entrez le montant de votre revenue " +business_user+ ":\n"))
      

      # cursor.execute(
      # "CREATE TABLE GestionDeRevenu (id INTEGER PRIMARY KEY AUTOINCREMENT,TypeBusiness TEXT, ChiffreBusiness TEXT)")

      new_user = (cursor.lastrowid, business_user , Montnat_business)

      cursor.execute('INSERT INTO GestionDeRevenu VALUES(?,?,?)',new_user)

      print("De nouvelle donner sont ajouter !!!")
      
    

    elif option == 3:
      print("\nAffichage des raports de Depenses !!!\n")

      aff = cursor.execute("SELECT * FROM GestionDeDepense")
      for row in aff.fetchall():
        print(row)



      print("\nVoici les donnees de votre Depense Effectuer !!!\n")

    elif option == 4:
      print("\nAffichage du raports des Revenus !!!\n")

      aff = cursor.execute('SELECT * FROM GestionDeRevenu')
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

      cursor.execute('INSERT INTO EcartDepenseRevenu VALUES(?,?,?,?)', new_user)
      connection.commit()

      text = "\tL'ecart du Depense et du Revenu effectuer est  : {} FCFA "
      print(text.format(Ecart))
      print("\nCes nouvelles donner de l'Ecart entre Depence et revenu sont ajouter !!!")

    else :
      print("vous avez choisissez une mauvaise option. Choisissez entre  0, 1, 2, 3, 4 or 5 ")
      print("")
      continue
        
except Exception as e:
    print("[ERREUR]", e)
    connection.rollback()

finally:  
      connection.close()
