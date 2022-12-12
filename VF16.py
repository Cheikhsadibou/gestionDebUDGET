"""
liste[X] ---> affiche ellement d'indic X
liste[-X] ---> affiche xieme element en partant de la            fin
liste[:] ---> affiche tout les elements 
liste[:X] ---> affiche les X premiers elements 
liste[X:] ---> affiche les X derniers elements 
liste[a:b] ---> affiche l'element de l'indice  A à l'élémenyt d'indice B (B exclue)  

===> object_à_suprimer = inventaire.index("fleche")
del inventaire[object_à_suprimer]

===> inventaire.remove("tunique")
print(inventaire[:])

===> sort ou reverse :permet de trier une liste de magnére croissant ou decroissante
EX : inventaire.sort()
print(inventaire[:])
===> cont : pour compter le nombre d'element citer dans cette liste
EX : print("nombre de potion  nommer est :",inventaire.count("potion"))

print(inventaire[:])

len(<liste>) = taille de notre liste(nombre d'element)
insert = inserer des elements dans le liste
append = inserer des elements direct dans le liste
remove = suprimer des elements dans la liste
join = permet de quiter une liste pour revenir à une phrase :
 EX :inventaire = ["bonjour", "tout", "le", "monde"]

phrase = "_".join(inventaire)
print(phrase) 

"""

# creer un liste 
""""
inventaire = range(20)
i = 0

while i < len(inventaire):
  print(inventaire[i])
  i += 1

"""
""" inventaire = range(20)

for valeur in inventaire:
  print(valeur)

"""
"""
import copy

liste1 = ["arc", "epee", "fleche", "bouclier", "chevalle de bataille"]
# NE fait pas de copy --> liste2 = liste1
liste2 = copy.deepcopy(liste1)

print("liste 1 ",liste1[:])
print("liste 1 ",liste1[:])

liste2.append("potion de mana")

print("liste 1 ",liste1[:])
print("liste 2 ",liste2[:])
"""
"""
===> pour afficher des elements avec leur indice
EX :
liste1 = ["arc", "epee", "fleche", "bouclier", "chevalle de bataille"]


for indice_object, valeur_object in enumerate(liste1):
  print("element d'indice {} -> {}".format(indice_object , valeur_object))
"""
liste1 = ["arc", "epee", "fleche", "bouclier", "chevalle de bataille"]


for k , v in enumerate(liste1):
  print("element d'indice {} -> {}".format(k, v))

