import tkinter
#from tkinter import*

mainapp = tkinter.Tk()
mainapp.title("mon premier programme ")
#mainapp.minsize(640, 480)
#mainapp.resizable(width=False, height=False)
#mainapp.maxsize(1200, 800)
#mainapp.positionfrom("user")
#mainapp.sizefrom("user")
#mainapp.geometry(X x Y+0+0)
mainapp.geometry("800x600+50+100")
"""
position_X = (largeur_ecran // 2) -     (largeur_fenetre  // 2)
position_Y = (largeur_ecran // 2) - (largeur_fenetre  // 2)

==>(pour modifier le titre de page web )
mainapp.tittle("mon premier programme")

"""

screen_x = int(mainapp.winfo_screenwidth())
screen_Y = int(mainapp.winfo_screenheight())
window_X = 800
window_Y = 500

pos_X = (screen_x // 2) - (window_X  // 2)
pos_Y = (screen_Y // 2) - (window_Y  // 2)

geo = "{}x{}+{}+{}".format(window_X, window_Y,screen_x,screen_Y)
mainapp.geometry(geo)

mainapp.mainloop()
