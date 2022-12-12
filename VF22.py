
"""
===> le widget qui permet de creer une case à coché 
check_widget = tkinter.Checkbutton(app)
check_widget.pack()

===> widget qui te permet de selectionner un "homme" oubien "femme"
ex: radio_widget = tkinter.Radiobutton(app, text="homme", value=1)
radio_widget2 = tkinter.Radiobutton(app, 
text="femme", value=0)

===>le widget qui te permet de creer une button qui glisse veeticalement de 0 à 100
ex : app = tkinter.Tk()
scale_W=tkinter.Scale(app)
Spinbox_widget = tkinter.Spinbox(app, <parametre>from_= ,to= )

===> le widget pour selectionner des elements : 
ex : lb = tkinter.Listbox(app)
lb.insert(1, "window")

"""

import tkinter
from tkinter import messagebox

app = tkinter.Tk()

def show_modal_window():
  messagebox.showerror("ERREUR", "Une probleme est survenue ")

btn = tkinter.Button(app, text="Déclencher une Erreur ", command=show_modal_window )


btn.pack()
app.mainloop()