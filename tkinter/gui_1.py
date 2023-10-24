from tkinter import *
import ttkbootstrap as ttk
import tkinter as tk
import sys

class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])

        #binds
        self.bind('<Escape>', lambda event: sys.exit())

        #widgets - 2 mainframes (menu, main)
        self.menu = Menu(self)
        self.main = Main(self)
        

        #run
        self.mainloop()


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()
        self.place(relx=0, rely=0, relwidth=0.4, relheight=1)

    def create_widgets(self):
        
        #widgets
        button_left_1 = ttk.Button(self, text='Button 1')
        button_left_2 = ttk.Button(self, text='Button 2')
        button_left_3 = ttk.Button(self, text='Button 3')

        scale1 = ttk.Scale(self, orient='vertical' )
        scale2 = ttk.Scale(self, orient='vertical' )

        #checkbox_frame & widgets
        checkbox_frame = ttk.Frame(self)
        check1 = ttk.Checkbutton(checkbox_frame, text='Check 1')
        check2 = ttk.Checkbutton(checkbox_frame, text='Check 2')
        

        #bottom entry
        bottom_entry = ttk.Entry(self)

        #grid
        self.columnconfigure((0,1,2) ,weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')

        
        #layout
        button_left_1.grid(row= 0, column= 0, columnspan=2, sticky='nsew', padx=2, pady=2)
        button_left_2.grid(row= 0, column= 2, sticky='nsew', padx=2, pady=2)
        button_left_3.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=2, pady=2)
        
        scale1.grid(row=2, column=0, sticky='nswe', padx=2, pady=10, rowspan=2)
        scale2.grid(row=2, column=2, sticky='nswe', padx=2, pady=10, rowspan=2)

        
        check1.pack(side='left', padx=2, pady=2)
        check2.pack(side='left', padx=2, pady=2)
        checkbox_frame.grid(row=4, column=0, columnspan=3)

        bottom_entry.place(relx=0.5, rely=0.97, relwidth=0.7, relheight=0.03, anchor='center')
        
        


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)
        
        self.create_widgets()


    def create_widgets(self):
            #widgets
            self.main_left = Main_left(self)
            self.main_right = Main_right(self)


class Main_left(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(side='left', expand=True, fill='both', padx= 2, pady=2)

        self.create_widgets()

    
    def create_widgets(self):
        
        #widgets
        label_frame_left = ttk.Label(self, text='Label 1', background='red')
        button_frame_left = ttk.Button(self, text='Button 1')

        #layout
        label_frame_left.pack(expand=True, fill='both', padx= 2, pady=2)    
        button_frame_left.pack(expand= True, fill='both', padx= 2, pady=2)  


class Main_right(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(side='right', expand=True, fill='both', padx= 2, pady=2)

        #widgets
        label_frame_right = ttk.Label(self, text='Label 2', background='blue')
        button_frame_right = ttk.Button(self, text='Button 2')

        #layout
        label_frame_right.pack(expand=True, fill='both', padx= 2, pady=2)
        button_frame_right.pack(expand= True, fill='both', padx= 2, pady=2)
       



App('Test GUI', (600,600))



