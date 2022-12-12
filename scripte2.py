"""
operateur en python : + addition 
                      - soustraction 
                      / division 
                      * multiplication 
                      % (modulo) --> reste d'une division euclidiene
variable = variable + X
variable + = X 

variable  = varible - X 
variable - = X

variable = variable * X 
variable * = X 
operateur de comparaison : == (égal à)
                          != (differant)
                          < (plus petit)
                          > (plus grand)
                          <= (plus petit ou egal à)
                          >= (plus grands ou egal à)
condition multiple       : and (et)
                          or (ou)
                          in \ not in (dans \ pas dans )
mots clee des conditions : if / elif / else 

"""

Identifient = "sadibou"
mots_de_passe = "password123"

print("interface de connection ")

user_id = input("veuiller saisir votre identifiant :")
user_password = input("veuiller saisir votre mots passe : ")
if user_id == Identifient  and user_password == mots_de_passe :  
    texte = "bravo {} vous ete connecter"

print(texte.format(user_id))