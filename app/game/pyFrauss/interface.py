# -*- coding: utf-8 -*-
import tkinter
import sys
import  os

from app.utils import menu


class Interface(tkinter.Frame):
    def __init__(self, windows, **kwargs):
        tkinter.Frame.__init__(self, windows, bg='black', width=800, height=600, relief=tkinter.SUNKEN, **kwargs)
        self.pack(fill=tkinter.BOTH)
        self.initMenu()

    def initWidget(self):
        pass

windows = tkinter.Tk()
windows.resizable(False, False)
windows.title("PyFauss")
interface = Interface(windows)
interface.mainloop()