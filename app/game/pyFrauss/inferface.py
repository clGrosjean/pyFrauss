# -*- coding: utf-8 -*-
import tkinter

class Interface(tkinter.Frame):
    def __init__(self, windows, **kwargs):
        tkinter.Frame.__init__(self, windows, bg='black', width=800, height=600, relief=tkinter.SUNKEN, **kwargs)
        self.pack(fill=tkinter.BOTH)
        self.initMenu()


    def initWidget(self):
        pass

    def initMenu(self):
        menuBar = tkinter.Menu(windows, selectcolor='blue')

        menuJeux = tkinter.Menu(menuBar, tearoff=1, bg='red')
        menuJeux.add_command(label="Jeu 1",command= self.cake)
        menuJeux.add_command(label="Jeu 2",command= self.cake)
        menuJeux_1 = tkinter.Menu(menuJeux)
        menuJeux_1.add_command(label="cake", command=self.cake)
        menuJeux.add_cascade(label="Cake", menu=menuJeux_1)
        menuJeux.add_separator()
        menuJeux.add_command(label="Quitter", command= self.undisplay)
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

        windows.config(menu=menuBar)

    def cake(self):
        print("cake")

    def undisplay(self):
        windows.destroy()

    def display(self):
        windows.mainloop()

    def pleinEcran(self):
        windows.attributes('-fullscreen',1)



windows = tkinter.Tk()
windows.resizable(False, False)
windows.title("PyFauss")
interface = Interface(windows)
interface.mainloop()