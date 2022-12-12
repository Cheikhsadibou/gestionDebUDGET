"""
propriete    : maniere de  manipuler/controler les  attributs
              principe d'encapsulation 
"""
class avatare:
  """ cette classe represente un avatare  """


  def __init__(self, name, old):
    print("creation d'avatare...")
    self.nom = name
    self._age = old
  
  def _getage(self):
    try:
        return self._age
    except AttributeError :
        print("l'age n'existe pas !!!")

  def _setage(self, nouvel_age):
      if nouvel_age < 0:
        self._age = 0
      else : 
        self._age = nouvel_age
  def _delage(self):
    del self._age

# property = (<getter>, <setter>, <delleter>, <helper>)
  age = property( _getage, _setage, _delage, "je suis l'age d'un avatare !!!")

# programme principale 
a1 = avatare("sadibou", 28)

help(avatare)





TYPE_DE_REVENUE
TYPE_DE_VERSEMENT
type_de_raport
CATEGORIE_DU_REVENUE           = []
Ecart_entre_depense_et_revenue,
ECART_ENTRE_DEPENSE_ET_REVENUE.append(Ecart_entre_depense_et_revenue)
CATEGORIE_DU_REVENUE.append(categorie_du_revenue)
db['categorie_du_revenue'] = CATEGORIE_DU_REVENUE
VERSEMENT                      = []
MONTANT_DU_REVENUE             = []
type_de_raport                 = []
db['type_de_depence'] = TYPE_DEPENSE


 items = [
   db{'serveur_user'} = SERVEUR_USER
  db{'Enregistrer_depense'} = ENREGISTER_DEPENSE
  db{'Enregistrer_revenue'} = ENREGISTRER_REVENUE
  db{'Montnat'} = MONTANT
  db{'Ecart_type'}  = ECART_TYPE
  db{'type_de_revenue'} = TYPE_DE_REVENUE
  db{'date'} = DATE
  ]


  db.update({'year': 1})
  db.all()

    return serveur_user, Enregistrer_depense, Enregistrer_revenue, Montnat, Ecart_type, type_de_revenue, dépense_type, date