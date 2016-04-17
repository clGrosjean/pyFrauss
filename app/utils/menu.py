import tkinter


class Menubar():
    def __init__(self, windows, color):
        self.windows = windows
        self.color = color

    def initMenu(self):
        menuBar = tkinter.Menu(self.windows, selectcolor='blue')

        menuJeux = tkinter.Menu(menuBar, tearoff=1, bg=self.color)
        menuJeux.add_command(label="Jeu 1", command=self.cake)
        menuJeux.add_command(label="Jeu 2", command=self.cake)
        menuJeux_1 = tkinter.Menu(menuJeux)
        menuJeux_1.add_command(label="cake", command=self.cake)
        menuJeux.add_cascade(label="Cake", menu=menuJeux_1)
        menuJeux.add_separator()
        menuJeux.add_command(label="Quitter", command=self.undisplay)
        menuBar.add_cascade(label="jeux", menu=menuJeux)

        menuParam = tkinter.Menu(menuBar, title='Paramètres', tearoff=0)
        menuParam.add_command(label="configuration")
        menuParam.add_command(label="Plein écran", command=self.pleinEcran)
        menuBar.add_cascade(label="paramètre", menu=menuParam)
        # menuParam.add_command(label="plein écran", command= self.pleinEcran)
        # menuBar.add_checkbutton(label="pleine écran", menu=menuParam)

        menuClassement = tkinter.Menu(menuBar, title='Classement', tearoff=0)
        menuClassement.add_command(label="Classement général")
        menuBar.add_cascade(label="Classement", menu=menuClassement)

        # menuAide = tkinter.Menu(menuBar, title='Aide', tearoff=0)

        self.windows.config(menu=menuBar)

    def cake(self):
        print("the cake is a lie")

    def undisplay(self):
        self.windows.destroy()

    def display(self):
        self.windows.mainloop()

    def pleinEcran(self):
        self.windows.attributes('-fullscreen', 1)
