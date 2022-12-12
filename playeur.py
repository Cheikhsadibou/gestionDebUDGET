

def parler (personnage , message):
    print("{} : {}".format(personnage , message))

def Au_revoir(): 
    print("Au_revoir")

if __name__== "scripte":
    print("phase de texte de playeur") 
    parler("adama" , "salut tout le monde")
    Au_revoir()