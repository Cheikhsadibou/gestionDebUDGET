
from math import*
import sqlite3


print("interface du getion de Budget")

# partit d'identification

print("")
user_id = input("veuiller saisir votre nom : ")

try:  
    user_id = str(user_id)
    print("")
    print("Entrer votre mots de passe : ")
except ValueError:
  print("Ceux que vous avais saisis est incorrect")
except NameError:
  print("veuiller saisir un nom valide")
else:
  print("vous avez valider votre nom Saisissez votre mots de passe")



passWord = input("veuiller saisir votre mots de passe : ")
print("identifiant valider")

name_user = user_id
mot_de_passe = passWord

if user_id == name_user and passWord == mot_de_passe:
  print("Vous etes connecter , bienvenue ", user_id)

# partie d'enregistrement de ces depenses 
class fiche:
  
      num    = "" 
      nom    = ""
      prenom = ""
      Enreg  = ""

fiche = user_id

def saisir():
  user_id.num   = int(input("Entrer votre numero de compte : "))
  user_id.Enreg = int(input("Entrer le montant à enregitrer :"))

def Affiche():
  print("Num : ", user_id.num)
  print("montant : ", user_id.Enreg)

saisir()
Affiche()

#De voir l'écart qui est entre ses dépenses et ses revenus

X = int(input("Donner la valeur des depenses effectuez : "))
Y = int(input("Donner la veleur des revenues effectuez : "))

if X <= Y:
  Ecart = X - Y
else:
  Ecart= Y - X
  print(Ecart) 