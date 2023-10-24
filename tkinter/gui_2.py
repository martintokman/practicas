#Create a GUI with 4 widgets, each with a different color and title. 
#Use classes and inheritance to create the widgets.
#Create a generic widget class that can be used to create the 4 widgets using parameters for setting
#the title of the labels, background color and button label.

from tkinter import *
import ttkbootstrap as ttk
import tkinter as tk
import sys


#Main window
class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        #binds
        self.bind('<Escape>', lambda event: sys.exit())

        #widgets
        Mywidget(self, 'Title 1', 'blue', 'Button 1')
        Mywidget(self, 'Title 2', 'green', 'Button 2')
        Mywidget(self, 'Title 3', 'yellow', 'Button 3')
        Mywidget(self, 'Title 4', 'red', 'Button 4')

        #run
        self.mainloop()

#Generic widget
class Mywidget(ttk.Frame):
    def __init__(self, parent, label_title, label_background, button_label):
        super().__init__(parent)

        self.label_title = label_title
        self.label_background = label_background
        self.button_label = button_label
        

    
        ttk.Label(self, text=label_title, background=label_background).pack(fill='both', expand=True, padx=5, pady=5)
        ttk.Button(self, text=button_label).pack(fill='both', expand=True, padx=5, pady=5)

        self.pack(fill='both', expand=True, side='left')

App('GUI - 2', (800, 600))