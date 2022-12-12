"""
isinstansce(<object> , <classe>): verifie qu'un object est de la classe renseigné

issubclass(<classe fille>, <class mére>): verifie qu'une classe est fille d'un autre 
"""


# classe mere 

class animal:

  def __init__(self, name):
    self.nom = name

  def manger(self):
    print(self.nom, "mange ")


class réptile(animal):
   
   def __init__(self, name, regime_alimentaire):
    animal.__init__(self, name,)
    self.regiment = regime_alimentaire 

   def manger(self):
    print("le réptile n'as pas d'oreille visible ...")


#programme principale 

serpent = réptile("cobra", "grenouille")

if issubclass(réptile, animal):

  print("le reptile herite d'animal ")
      

    