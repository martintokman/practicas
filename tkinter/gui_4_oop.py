import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GUI - 4 - Procedural')
        self.geometry('600x400+50+50')
        
        #binds
        self.bind('<Escape>', lambda event: self.destroy())

        #Mainframe
        self.main_frame = Mainframe(self)
        
        #run
        self.mainloop()


class Mainframe(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        def open_window():
            button_1.configure(state='disabled')    
            button_2.configure(state='enabled')
            self.new_window = tk.Toplevel(self)
            self.new_window.title('Extra window')
            self.new_window.geometry('400x300+600+300')
            self.new_window.focus_force()
            self.new_window.bind('<Escape>', lambda _: close_window())
            self.new_window.protocol("WM_DELETE_WINDOW", close_window)
            label = ttk.Label(self.new_window, text='This is an extra window') 

            #Widgets
            button = ttk.Button(self.new_window, text='Close extra window', command=close_window)

            #layout
            label.pack(pady=20)
            button.pack(pady=20)

        def close_window():
            button_1.configure(state='enabled')
            button_2.configure(state='disabled')
            self.new_window.destroy()

        
        #widgets
        button_1 = ttk.Button(self, text='Open extra window', command= open_window)
        button_2 = ttk.Button(self, text='Close extra window', command= close_window, state='disabled')
        button_3 = ttk.Button(self, text='Create yes/no message', command=lambda: print(tk.messagebox.askyesno('Yes/No message', 'Do you want to continue?')))
        button_4 = ttk.Button(self, text='Create info message', command=lambda: print(tk.messagebox.showinfo('Info message', 'This is an info message')))
        button_5 = ttk.Button(self, text='Create warning message', command=lambda: print(tk.messagebox.showwarning('Warning message', 'This is a warning message')))
        button_6 = ttk.Button(self, text='Close program', command=parent.destroy)

        #layout
        button_1.pack(pady=20)
        button_2.pack(padx=20)
        button_3.pack(pady=20)
        button_4.pack(padx=20)
        button_5.pack(pady=20)
        button_6.pack(padx=20)

        #run
        self.pack()


App()

