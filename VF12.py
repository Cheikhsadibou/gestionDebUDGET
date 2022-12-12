"""==> metode           : c'est une fonction d'une classe (ex : manger , boire , dormir , parler , marcher ,mourir ,etc ...)

==> metode de classe : c'est une conction d'une classe (explication à venir )

==> metode statique  :c'est une fonction de la classe , mais independent de la classe 
"""

class avatare:
  """ class qui definie un avatare  """
  
  lieu_habitation = "terre"

  def __init__(self, name, old):
    self.nom = name 
    self.age = old

  def parler(self, message):
    print("{} à dit : {}".format(self.nom, message))

  def changer_planete(cls, nouvelle_planete ):
    avatare.lieu_habitation = nouvelle_planete

  changer_planete = classmethod(changer_planete)

  def definition():
    print("l' humain est classer le plus haut etre vivant de la chaine alimentaire")

  definition = staticmethod(definition)

# progrmme principale 

avatare.definition()
a1 = avatare("sadibou", 28)

print("planete_actuelle".format(avatare.lieu_habitation))

avatare.changer_planete("mars")

print("planete_actuelle".format(avatare.changer_planete))