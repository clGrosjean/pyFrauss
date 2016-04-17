import tkinter


class Menubar:


    def __init__(self, windows, color):
        self.windows = windows
        self.color = color
        self.isFullscreen = tkinter.IntVar()
        self.isSwag = tkinter.IntVar()

    def initMenu(self):
        menuBar = tkinter.Menu(self.windows)

        menuJeux = tkinter.Menu(menuBar, tearoff=1, bg=self.color)
        menuJeux.add_command(label="Jeu 1", command=self.cake, activebackground='#BABABA')
        menuJeux.add_command(label="Jeu 2", command=self.cake, activebackground='#BABABA')
        menuJeux_1 = tkinter.Menu(menuJeux)
        menuJeux_1.add_command(label="cake", command=self.cake,activebackground='#BABABA')
        menuJeux.add_cascade(label="Cake", menu=menuJeux_1)
        menuJeux.add_separator()
        menuJeux.add_command(label="Quitter", command=self.undisplay, activebackground='#29FADE')
        menuBar.add_cascade(label="jeux", menu=menuJeux)

        menuParam = tkinter.Menu(menuBar, title='Paramètres', tearoff=0)
        menuParam.add_command(label="configuration")
        menuBar.add_cascade(label="paramètre", menu=menuParam)


        menuParam.add_checkbutton(label="Plein écran", variable=self.isFullscreen, onvalue=1 ,offvalue=0, command=self.pleinEcran, selectcolor="blue")
        menuParam.add_checkbutton(label="Swag Mode", variable=self.isSwag, command=self.swag)

        menuClassement = tkinter.Menu(menuBar, title='Classement', tearoff=0)
        menuClassement.add_command(label="Classement général")
        menuBar.add_cascade(label="Classement", menu=menuClassement)

        menuAide = tkinter.Menu(menuBar, title='Aide', tearoff=0)
        menuAide.add_command(label="À propos", command= self.propos)
        menuBar.add_cascade(label="Aide", menu=menuAide)

        self.windows.config(menu=menuBar)

    def cake(self):
        print("the cake is a lie")

    def undisplay(self):
        self.windows.destroy()

    def display(self):
        self.windows.mainloop()

    def pleinEcran(self):
        self.windows.attributes('-fullscreen', self.isFullscreen.get())

    def swag(self):
        if self.isSwag.get() == 1:
            pass
        else:
            pass


    def propos(self):
        pass
