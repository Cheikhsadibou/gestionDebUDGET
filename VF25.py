"""
===>add_checkbutton
===>add_radiobutton
===>add_separator
"""

#creationde la fenetre + le prametrage 

import tkinter
def show_about():
  show_window = tkinter.Toplevel(app)
  show_window.title("nouveau fenetre")
  lb = tkinter.Label(show_window, text="bienvenue sur votre nouveau fenetre ")
  lb.pack()

def hello():
  print("coucou monsieur")


#creation de fenetre + le parametrage 
app = tkinter.Tk()
app.geometry("640x480")
app.title("creation de menu")


#widget
VF25Menu = tkinter.Menu(app)

first_menu = tkinter.Menu(VF25Menu, tearoff=0)
first_menu.add_command(label="option1", command=hello)
first_menu.add_command(label="option2")
first_menu.add_separator()
first_menu.add_command(label="Quitter", command=app.quit)


second_menu = tkinter.Menu(VF25Menu, tearoff=0)
second_menu.add_command(label="programme1")
second_menu.add_command(label="Autre fenetre", command=show_about)


VF25Menu.add_cascade(label="parametre1", menu=first_menu)
VF25Menu.add_cascade(label="parametre2", menu=second_menu)



# boucle principale
app.config(menu=VF25Menu)
app.mainloop()