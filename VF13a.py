class avatare: 

  def __init__(self, name, old):
    self.nom = name
    self._age = old

  def _getage(self):
    if self._age <= 1:
      return "{} {} ".format(self._age, "an")
    else:
      return "{} {} ".format(self._age, "ans")

  # property (<getter>, <setter>, <deleter>, <help>)

  age = property( _getage)
age = input("Definisser votre ages:")

# programme principale
 
a1 = avatare("sokhna laye ", 1)

print("{}  a  {}  ".format(a1.nom, a1.age))