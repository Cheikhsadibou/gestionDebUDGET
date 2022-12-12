"""
===> pour calculer le temps exacte qui s'est ecouler : 
import time 

begin = time.time()
print("debut")

time.sleep(5)

end = time.time()
print("fin")

print(f"temps exacte ecoulé :{end-begin}s ") 

            localtime()
(TIMESTAMP)---------------> stucture du temps 
           <--------------
             mktime()
ex :

import time 

tps = time.localtime()

print(tps)

tps = time.mktime(tps)

print(tps)

%d : (01 à  31)
%m : (01 à 12)
%Y : année (ex = 2022) - %y (00 à 99)
%H : heure (00  à 23)
%I : minutes (00 à 59)
%S : seconds (00 à 59)

%A : jour semaine / %a (jour abrégé)
%B : mois   / %b (mois abrégé)

%Z : fuseau horaire (timeZone)
"""


import time


print(time.strftime("%Z"))

