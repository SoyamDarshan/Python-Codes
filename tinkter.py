# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 01:51:31 2018

@author: soyam
"""

from tkinter import *
class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        
        self.master = master
        
root = Tk()


app = Window(root)

root.mainloop()        