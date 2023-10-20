from tkinter import *
import ttkbootstrap as ttk
import tkinter as tk
import sys




#window
window = ttk.Window()
window.geometry('600x600')

window.bind('<Escape>', lambda event: sys.exit())


#mainframes
frame_left = ttk.Frame(window)

#configure frame_left grid
frame_left.columnconfigure((0,1,2) ,weight=1, uniform='a')
frame_left.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')


#frame_left widgets
button_left_1 = ttk.Button(frame_left, text='Button 1')
button_left_2 = ttk.Button(frame_left, text='Button 2')
button_left_3 = ttk.Button(frame_left, text='Button 3')

scale1 = ttk.Scale(frame_left, orient='vertical' )
scale2 = ttk.Scale(frame_left, orient='vertical' )

#checkbox_frame & widget
checkbox_frame = ttk.Frame(frame_left)
check1 = ttk.Checkbutton(checkbox_frame, text='Check 1')
check2 = ttk.Checkbutton(checkbox_frame, text='Check 2')

bottom_buttom = ttk.Button(frame_left)



frame_right = ttk.Frame(window)
frame_right_1 = ttk.Frame(frame_right)
frame_right_2 = ttk.Frame(frame_right)


#widgets right frame 
label_right_1= ttk.Label(frame_right_1, text='Label 1', background='red')
button_right_1= ttk.Button(frame_right_1, text='Button 1')

label_right_2= ttk.Label(frame_right_2, text='Label 2', background='blue')
button_right_2= ttk.Button(frame_right_2, text='Button 2')




#layout
frame_left.place(relx=0, rely=0, relwidth=0.4, relheight=1)
frame_right.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)

frame_right_2.place(relx=0, rely=0, relwidth=0.5, relheight=1)
frame_right_1.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

label_right_1.pack(expand=True, fill='both', padx= 2, pady=2)
label_right_2.pack(expand=True, fill='both', padx= 2, pady=2)

button_right_1.pack(expand= True, fill='both', padx= 2, pady=2)
button_right_2.pack(expand= True, fill='both', padx= 2, pady=2)

button_left_1.grid(row= 0, column= 0, columnspan=2, sticky='nsew', padx=2, pady=2)
button_left_2.grid(row= 0, column= 2, sticky='nsew', padx=2, pady=2)
button_left_3.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=2, pady=2)

scale1.grid(row=2, column=0, sticky='nswe', padx=2, pady=2, rowspan=2)
scale2.grid(row=2, column=2, sticky='nswe', padx=2, pady=2, rowspan=2)

check1.pack(side='left', padx=2, pady=2)
check2.pack(side='left', padx=2, pady=2)
checkbox_frame.grid(row=4, column=0, columnspan=3)

bottom_buttom.grid(row=5,column=0, columnspan=3, sticky='nsew', padx=2, pady=2)


#run
window.mainloop()






















'''
#frames A/B van con place

#widgets
frame_a = ttk.Frame(window)
frame_b = ttk.Frame(window)

#frame A widgets
button1 = ttk.Button(frame_a)
button2 = ttk.Button(frame_a)
button3 = ttk.Button(frame_a)
scale1 = ttk.Scale(frame_a)
scale2 = ttk.Scale(frame_a)
check1 = ttk.Checkbutton(frame_a, text='Check 1')
check2 = ttk.Checkbutton(frame_a, text='Check 2')
bottom_buttom = ttk.Button(frame_a)



#frame B widgets

#sub frames
frame_b1 = ttk.Frame()
frame_b2 = ttk.Frame()


#frame B_1 widgets
label_frame_b1 = ttk.Label(frame_b1, text = 'Label 1', background='red')
button_frame_b1 = ttk.Button(frame_b1, text='Button 1')



#frame B_2 widgets
label_frame_b2= ttk.Label(frame_b2, text = 'Label 2', background='blue')
button_frame_b2 = ttk.Button(frame_b2, text='Button 1 ')


#layout

#main frames
frame_a.place(relx= 0, rely=0, relwidth=0.4, relheight=1)
frame_b.place(relx=0.25 , rely=0, relwidth=0.75, relheight=1)

#sub-frames
frame_b1.pack()
frame_b2.pack()


#frame A
button1.pack()
button2.pack()
button3.pack()
scale1.pack()
scale2.pack()
check1.pack()
check2.pack()
bottom_buttom.pack()

#frame B
label_frame_b1.pack()
button_frame_b1.pack()

label_frame_b2.pack()
button_frame_b2.pack()'''