"""
creation d'un dictionaire : dico = {} # vide 
                          : dico = {<cle>:valeur, <cle2>:valeur }
Acces à une valeur         : dico[<cle>]
ajouter au  dictionner     : dico[<clee>] = <valeur>
supression                 : dico.pop(<clee>)
                            del dico[<clee>]
afficher les clees         : for key in dico.keys()
                            print(key)
afficher les valeurs       : for key in dico.values()
                            print()
copy de dictionnaire       : dico1 = {"12": "bonjour", "34":"sa vas"}
                            dico2 = dico.copy()                          
"""

def maFonctionBizar(**parametres):
  print(parametres)

maFonctionBizar(g = "sadibou", s = "sokhna")
