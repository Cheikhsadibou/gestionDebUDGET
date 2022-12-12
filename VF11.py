class avatar:
  """
classe des avatares
  """
  avatare_creer = 1
 
  def __init__(self , name , old):
    print("creation d'une avatare numero {} : ".format(avatar.avatare_creer))

    self.prenom = name
    self. ages = old
    avatar.avatare_creer += 1

print("lencement d'une programme ...")
prenom =input("veuillez saisir votre nom : ")
ages = int(input("veuiller saisir votre ages : "))

print("le prenom de l'avatare 1 est {}  ".format(prenom.prenom))
print("l'ages de lavatare 1 est {} ans ".format(ages.ages))
a2 = avatar("sokhna" , 20)
print("le prenom de l'avatare 2 est : {}".format(a2.prenom))
print("l'age de lavatare 2 est {} ans ".format(a2.ages))