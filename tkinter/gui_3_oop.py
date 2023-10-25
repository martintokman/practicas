import tkinter as tk
from tkinter import ttk
from random import randint, choice

#create class App for main window
class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0], size[1])
        
        #binds
        self.bind('<Escape>', lambda event: self.destroy())
        
        #widgets
        Canvas(self)
       
        
        #run
        self.mainloop()

#create class Canvas for canvas
class Canvas(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        canvas = tk.Canvas(self, bg = 'white', scrollregion=(0,0,2000,5000))
        canvas.create_line(0,0,2000,5000, fill='red', width=5)

        #create 100 random rectangles
        for i in range(100):
            x1 = randint(0, 2000)
            y1 = randint(0, 5000)
            x2 = x1 + randint(10, 500)
            y2 = y1 + randint(10, 500)
            canvas.create_rectangle(x1, y1, x2, y2, fill=choice(['red', 'blue', 'green', 'yellow', 'black']))

            #scrollbar  
            v_scrollbar = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
            h_scrollbar = ttk.Scrollbar(self, orient='horizontal', command=canvas.xview)
            canvas.configure(yscrollcommand=v_scrollbar.set)
            canvas.configure(xscrollcommand=h_scrollbar.set)

            #mousewheel scrolling vertically
            canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), 'units'))

            #mousewheel scrolling horizontally crtl + mousewheel
            canvas.bind('<Control-MouseWheel>', lambda event: canvas.xview_scroll(int(-1*(event.delta/120)), 'units'))


            #layout
            canvas.pack(fill='both', expand=True)
            v_scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')
            h_scrollbar.place(relx=0, rely=1, relwidth=0.97, anchor='sw')

            self.pack(fill='both', expand=True)

#runn app
App('GUI - 3 - OOP', (800, 600))
