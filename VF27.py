
"""
d1 = datetime.datetime(2022, 11, 15, 10, 22, 44)
d2 = datetime.datetime(2022, 11, 16, 10, 27, 44,)

print(d1.year)
print(type(d1))

===> pour consulter l'heure  :
from datetime import datetime

print(datetime.now()) 


===> l'autre exemple pour afficher l'heure:
from datetime import date

now =date.today()
print(now)
"""

import datetime
from datetime import date

now = date.today()

born = datetime.date(1994, 8, 5)

print(f"{now.year - born.year}ans")

