"""
===> pour les processueses qui s'execute chaqu'un dans le en memme temps :
ex : import time
import threading


def process_one():
  i = 0
  while i < 3:
    print("oooooooooo")
    time.sleep(0.3)
    i += 1

def process_two():
  i = 0
  while i < 3:
    print("bonjour")
    time.sleep(0.3)
    i += 1

process_two()  

process_one()
th1 = threading.Thread(target=process_one)
th2 = threading.Thread(target=process_two)

th1.start()
th2.start()

th1.join()
th2.join()

print("fin du programme")

===>

"""
import time
import  threading

mon_clee = threading.RLock()

class mon_project(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)

  def run(self):
    i = 0
    while i < 3:
      with mon_clee:
        letters = "ABC"
        for lt in letters:
          print(lt)
          time.sleep(0.3)
      i += 1



th1 = mon_project()
th2 = mon_project()


th1.start()
th2.start()

th1.join()
th2.join()

print("Fin du programme")