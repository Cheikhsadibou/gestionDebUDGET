# classe mere 
class vehicule:

  def __init__(self, marque, consomation):
    self.nom = marque
    self. carburant = consomation

  def se_deplacer(self):
    print("le vehicule {} se deplace ... ".format(self.nom))

   


# classe fille 

class voiture(vehicule):
    
   def __init__(self, marque, consomation, puissance):
      vehicule. __init__(self, marque, consomation, )
      self.capaciter = puissance

   def se_deplacer(self):
      print("la voiture roule ...")


class avion(vehicule):

   def __init__(self, marque, consomation, marchandise):
      vehicule. __init__(self, marque, consomation)
      self.passager = marchandise
  
   def se_deplacer(self):
      print("l'avion survole ...")



# programme principale 
Voiture1 = voiture("toyota supra  ", 300, 500)
Voiture1.se_deplacer()
AV1 = avion("boing 377", 500, "personne")
AV1.se_deplacer()