"""
mode d'ouverture de texte : r (lecture seul)
                          : w (ecriture avec remplacement)
                          : a (eciture avec ajout en fin de fichier)
                          eX : nombre = 15
                            fic.write(str(nombre))
                          x (lecture et ecriture )
                          r+ (lecture et ecriture dans un méme fichier)
pour lire tout le  texte       :=>content = fic.read()
                                print(content)
                                =>content = fic.read()
                                print(content)
pour lire une seul ligne       : content = fic.readline()
                                print(content)
ecriture                       : fic.write()
"""


with open("donner", "w") as fic:

  nombre = 15 
  fic.write(str(nombre))
  fic.write("\n bonjour tout le monde ")
  fic.write("\n comment vas votre programme ")
  fic.write("\n bonne debut de week end\n")