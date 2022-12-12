"""
nommer une variable : doit commencer par un lettre                ou un underscord
                     --> ne pas contenir de caracteres spetiaux 
                     --> ne pas contenir de space 
                     --> utiliser des underscord
type standarts      : --> entiers numerique (int)
                      --> nombre flotant (float)
                      --> chaine de carataires (str)
                      --> boleen (bool)
fonction vue : print() --> afficher à l'ecran 
              input()  --> lire le clavier 
              str.format  --> formater une chaine 
              typt () --> retourne le type d'un donner """
"""
boucle  : while / for 
        : break  (casse la boucle ) / continue (revient au debut de la boucle )
"""
"""
fonction vue : int() input()
             : type() int() float() str() bool()
"""
"""
def dire (nom_personne , message_personne)
print ("{} , {} . format(nom_personne , message_personne "))
"""
"""def show_invectory(*list_items):
    for items in list_items:
      print(items)
      print("")



show_invectory("bonjour")
show_invectory("comment allez vous", "et la journé ")
"""
"""
calculer = lambda a , b : a + b 

print(calculer(432 , 653))
"""
"""
impoeter un module  : ==> import <nom du module>
                      ==>from <nom du module > import <nom_du_foction> 
                          ex : from MATH import sqrt
                          # print 
                          ex : <nom_du_fonction>("")
                          ex : parler("salut les abonnes)
                      ==>fom <nom_module> imort *
                      ==>import<nom_du_documents><nom_du_    modul>
                          : pour le print
                          --> <nom_du_documents> <nom_du_module(fichers)>.<nom_fonction>("")
                      ==> import <nom_du_document>.<nom_du_module(fichiers)> as <nom_du_module(fichers)>
                      : pour le print 
                      -->  <nom_du_module(fichers)>.<nom_fonction>("")
"""
"""
gerer les exeptions : try/except et (else/finally)

cas d'exception     : valueEROR
                      namEROR
                      typeEror
                      zeroDivisionEror
                      OSeror
                      AssertonEror
"""
"""
pour lever EXECEPTION c.a.d crer son propre exeptionError ........: 
try:
  ageUser =input("Quel est votre age : ")
  ageUser =int(ageUser)

  if ageUser > 25:
    raise InvalidContext("coucou !")
except InvalidContext :
  print("invalidContextError")
"""
"""
ASSERTION signifie ceux que vous souhaiter sur un nombre saisi par l'utilisateur c.a.d :
jeux veux la condition qui vienne apres soi valider sinon on léve une ASSERTION : 
try:
  ageUser = input("Quel est votre ages : ")
  ageUser = int(ageUser)

  assert ageUser > 25 # je veux que ages soit plus grand que 25 
except AssertionError:
  print("vous n'avez pas saisi ce que je souhaiter !")
"""

nombre1 = 400
nombre2 = input("veuiller choisir le nombre à diviser : ")
try:
    nombre2 = int(nombre2)
    print("resulta = {}".format(nombre1 / nombre2))
except ZeroDivisionError :
    print("zero n'est pas divible avec ceux nombre ! ")
except ValueError :
    print("ceux vous avez saisis est indivisible !")
except:
    print("valeur incorect ! ")
else :
    print("bravo vous avez saisis une valeur demander ! ")
finally:
    print("fin du programme de calcule ! ")
