import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#create extra window
def create_extra_window():

    #create window
    global extra_window
    extra_window = tk.Toplevel()
    extra_window.title('Extra window')
    extra_window.geometry('400x300+600+300')
    extra_window.focus_force()
    

    #binds
    extra_window.bind('<Escape>', lambda _: close_extra_window())
    extra_window.protocol("WM_DELETE_WINDOW", close_extra_window)

    
    
    #widgets
    label = ttk.Label(extra_window, text='This is an extra window')
    button = ttk.Button(extra_window, text='Close extra window', command=close_extra_window)
    
    #enable button_2
    button_2.config(state='enabled')

    #Disable "Create extra window" button
    button_1.config(state='disabled')

    #layout 
    label.pack(pady=20)
    button.pack(pady=20)
    

#Close extra window
def close_extra_window():

    #close extra window
    extra_window.destroy()

    #disable button_2
    button_2.config(state='disabled')
    button_1.config(state='enabled')


#window
window = tk.Tk()
window.title('GUI - 4 - Procedural')
window.geometry('600x400+50+50')

#binds
window.bind('<Escape>', lambda event: window.destroy())



#widgets
button_1 = ttk.Button(window, text='Open extra window', command=create_extra_window)
button_2 = ttk.Button(window, text='Close extra window', command=close_extra_window, state='disabled')
button_3 = ttk.Button(window, text='Create yes/no message', command=lambda: print(tk.messagebox.askyesno('Yes/No message', 'Do you want to continue?')))
button_4 = ttk.Button(window, text='Create info message', command=lambda: print(tk.messagebox.showinfo('Info message', 'This is an info message')))
button_5 = ttk.Button(window, text='Create warning message', command=lambda: print(tk.messagebox.showwarning('Warning message', 'This is a warning message')))
button_6 = ttk.Button(window, text='Close program', command=window.destroy)


#layout
button_1.pack(pady=20)
button_2.pack(padx=20)
button_3.pack(pady=20)
button_4.pack(padx=20)
button_5.pack(pady=20)
button_6.pack(padx=20)




#run
window.mainloop()