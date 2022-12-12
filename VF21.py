"""
<nom-variable> = <nom_label>(<widget_parent>, <paramatre>....)


===> boutont_quit =tkinter.Button(app, text="ok")
boutont_quit.pack() (pour l'affichage d'une bouton que l'on peut cliquer la dessus )

===> (l'attribut qui permet d'excuter une petit fonction )
EX : def hello():
  print("sokhna laye ndigne")
boutont_quit =tkinter.Button(app, command=(hello))

===> le widget : message_

"""

import tkinter 

app = tkinter.Tk()

def hello():
  print("j'ai vue")

Button_name = tkinter.Button(app, text="ok", command=hello)

Button_name.pack()
app.mainloop()