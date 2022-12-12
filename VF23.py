"""
StringVar()     : chaine de caractaire [str] 
IntVar()        : nombre entier [int]
DoubleVar()     : nombre flottant [float]
BooleanVar()    : Booleen [bool] 

"""

import tkinter
# observateur 
def update_observer(*args):
  print("j'ai vue ")

# creation et parametre de la fenetre 
app = tkinter.Tk()
app.geometry("400x300")
app.title("variable tkinter")

def update_label(*args):
  stringVar_widget.set(stringVar_widget2.get())

#widget
stringVar_widget2 = tkinter.StringVar()
stringVar_widget2.trace("w",update_label)
entry = tkinter.Entry(app, textvariable= stringVar_widget2)

stringVar_widget = tkinter.StringVar()
label =tkinter.Label(app, textvariable=stringVar_widget)
stringVar_widget.set("ici le texte de saisis")



entry.pack()
label.pack()
#boucle principale
app.mainloop()