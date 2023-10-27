# Create basic custom tkinter objects

import customtkinter as ctk

def set_light_dark_mode():
    mode_status = ctk.get_appearance_mode()
    print(mode_status)
    if mode_status == 'Light':
        ctk.set_appearance_mode('Dark')
    else:
        ctk.set_appearance_mode('Light')


# Window
window = ctk.CTk()
window.title('My window')
window.geometry('600x400')
window._set_appearance_mode('Light')


# Binds
window.bind('<Escape>', lambda event: window.destroy())

# Frames
frame = ctk.CTkFrame(window)

# Widgets
label_var = ctk.StringVar(value='A custom value')
label = ctk.CTkLabel(
    window,
    text='A label',
    fg_color=('blue', 'red'),
    text_color=('white', 'black'),
    textvariable=label_var,
    corner_radius=6,
)

button = ctk.CTkButton(window, text="Light/Dark mode", command= lambda:set_light_dark_mode() )
slider = ctk.CTkSlider(frame)
switch = ctk.CTkSwitch(window, text="a Swich", width=50, height=50, text_color=('black', 'white'))
label2 = ctk.CTkLabel(window, text='Press Esc to exit',
                      text_color=('black', 'white'))


# Layout
label.pack(pady= 10)
button.pack()
slider.pack(pady= 10)
frame.pack(pady=10)
switch.pack(pady=10)
label2.pack(pady=20)


# Run
window.mainloop()
