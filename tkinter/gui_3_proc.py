import tkinter as tk
from tkinter import ttk
from random import randint, choice

#setup
window = tk.Tk()
window.title('GUI - 3 - Scrolling')
window.geometry('600x400')

#binds
window.bind('<Escape>', lambda event: window.destroy())

#canvas
canvas = tk.Canvas(window, bg = 'white', scrollregion=(0,0,2000,5000))
canvas.create_line(0,0,2000,5000, fill='red', width=5)

#create 100 random rectangles
for i in range(100):
    x1 = randint(0, 2000)
    y1 = randint(0, 5000)
    x2 = x1 + randint(10, 500)
    y2 = y1 + randint(10, 500)
    canvas.create_rectangle(x1, y1, x2, y2, fill=choice(['red', 'blue', 'green', 'yellow', 'black']))

#scrollbar  
v_scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
h_scrollbar = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
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




#run
window.mainloop()
