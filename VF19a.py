import pickle

class player:

  def __init__(self, name, level):
    self.nom = name
    self.undegrund = level

  def whoamie(self):
    print("{} ({})".format(self.nom, self.undegrund))



#prohramme principale

p1 = player("sokhna", 20)

with open("player.data", "wb") as fic:
  record = pickle.Pickler(fic)
  record.dump(p1)
