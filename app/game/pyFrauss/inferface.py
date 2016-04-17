# -*- coding: utf-8 -*-
import tkinter
from app.utils import menu


class Interface(tkinter.Frame):
    def __init__(self, windows, **kwargs):
        tkinter.Frame.__init__(self, windows, bg='black', width=800, height=600, relief=tkinter.SUNKEN, **kwargs)
        self.pack(fill=tkinter.BOTH)
        self.initWidget()
        menu.Menubar.initMenu(menu.Menubar(windows, 'red'))

    def initWidget(self):
        pass


windows = tkinter.Tk()
windows.resizable(False, False)
windows.title("PyFrauss")
interface = Interface(windows)
interface.mainloop()
