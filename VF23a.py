import tkinter

def update_label(*args):
  if intVar.get():
    stringVar.set("C'est un homme")
  else:
    stringVar.set("C'est une femme")

app = tkinter.Tk()
app.title("variable widgets")

intVar = tkinter.IntVar()
intVar.trace("w", update_label)
Radiobutton = tkinter.Radiobutton(app, text="homme",value=1, variable=intVar)


Radiobutton2 = tkinter.Radiobutton(app, text="femme", value=0, variable=intVar)

stringVar = tkinter.StringVar()
var_label = tkinter.Label(app, textvariable=stringVar)

Radiobutton.pack()
Radiobutton2.pack()
var_label.pack()

app.mainloop()