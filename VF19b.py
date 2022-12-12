import pickle


class avatare:

    def __init__(self, name, level):
      self.nom = name
      self.undergrund = level

    def sadibou(self):
      print("{} ({})".format(self.nom, self.undergrund))

#programme principale 

with open("avatare", "rb") as fic:
  get_record = pickle.Unpickler(fic)
  avatareOne = get_record.load()

avatareOne.sadibou()