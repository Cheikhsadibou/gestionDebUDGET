"""
(!) tuple : conteneur immuable (dont on peut modifier les valeurs ) 

creation de tuple : mon_tuple = () #vide
                    mon_tuple = 17,# une seul valeur
                    mon_tuple =(17,)#idem qu'au dessus
                    mon_tuple = (4, 6)plusieur valeur

2 raisons d'utliser les tuples : affectation multiple de variable
                                : retour multiple de fonction 

"""


def get_player_positon():
    posX = 17
    posY = 14

    return(posX , posY)

# programme principale

coordX = 0
coordY = 0

print("position du jueur : ({}/{})".format(coordX, coordY))

(coordX,coordY) = get_player_positon()

coordX = 123
coordY = 123

print("position du jueur : ({}/{})".format(coordX, coordY))
