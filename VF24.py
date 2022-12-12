"""

===>le widget pour creer une petit cadre dans votre page web
ex : mainframe = tkinter.LabelFrame(app, text="gestion de budget", width=300, height=200, borderwidth=2)

===> pour le positionnement des widget on a : side= "tope"
side= "bottom"
expend= "1"
padX= 10,
padY= 5
===>btn.grid(row=0, column=3, columnspan=4)
sticky="ne"
btn.place(x= 500, y= 5)
"""



import tkinter
#creation et prametre de la fenetre
app = tkinter.Tk()
app.geometry("640x480")
app.title("positonnement widget")

#widget
label =tkinter.Label(app, text="ici le texte de saisis")

entry = tkinter.Entry(app)

btn = tkinter.Button(app, text="Bienvenue")



label.grid(sticky="ne")
entry.grid()
btn.grid(sticky="se")



#boucle principale
app.mainloop()