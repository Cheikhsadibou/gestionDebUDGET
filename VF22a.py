"""
===> le widget qui permet de ceer une message d'erreur :
import tkinter 
from tkinert import messagebox

def show_modal_window():
  messagebox.showerror("ERREUR", "une probleme est survenue ")
app = tkinter.Tk()
btn = tkinter.Button(app,text="Declencher une erreur ", commande= show_modal_window)

btn.pack()
app.mainloop()


===> il y'as aussi showerror
                   showinfo
                   showwarning
                   askquestion
                   askokcancel
                   askyesno
                   askretrycancel

"""



import tkinter
from tkinter import messagebox

def show_modal_window():
  messagebox.askretrycancel("SONDAGE", "quelle est votre choix ?")

app = tkinter.Tk()
btn = tkinter.Button(app, text="declencer une erreur", command = show_modal_window)

btn.pack()
app.mainloop()
