import ttkbootstrap as ttk
import tkinter as tk
import sys


# Main window
class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])

        # binds
        self.bind("<Escape>", lambda event: sys.exit())

        # widgets - 2 mainframes (menu, main)
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()


# Menu frame (left mainframe)
class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.create_widgets()
        self.place(relx=0, rely=0, relwidth=0.4, relheight=1)

    def create_widgets(self):
        Menu_row_0(self).pack(expand=True, fill="both", padx=2, pady=2)
        Menu_row_1(self).pack(expand=True, fill="both", padx=2, pady=2)
        Menu_row_2(self).pack(expand=True, fill="both", padx=2, pady=2)
        Menu_row_3_and_4(self).pack(expand=True, fill="both", padx=2, pady=2)
        Menu_row_5(self).pack(expand=True, fill="both", padx=2, pady=2)


class Menu_row_0(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        menu_row_0_button_1 = ttk.Button(self, text="Button 1")
        menu_row_0_button_2 = ttk.Button(self, text="Button 2")

        # create layout
        menu_row_0_button_1.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        menu_row_0_button_2.pack(side="left", expand=True, fill="both", padx=2, pady=2)


class Menu_row_1(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        menu_row_1_button_1 = ttk.Button(self, text="Button 1")

        # create layout
        menu_row_1_button_1.pack(side="left", padx=2, pady=2, expand=True, fill="both")


class Menu_row_2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create grid
        self.rowconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        # create widgets
        scale1 = ttk.Scale(self, orient="vertical")
        scale2 = ttk.Scale(self, orient="vertical")

        # create layout
        scale1.grid(row=0, column=0, sticky="nswe", padx=2, pady=10, rowspan=2)
        scale2.grid(row=0, column=2, sticky="nswe", padx=2, pady=10, rowspan=2)


class Menu_row_3_and_4(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create grid
        self.rowconfigure(0)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")

        # create widgets
        check1 = ttk.Checkbutton(self, text="Check 1")
        check2 = ttk.Checkbutton(self, text="Check 2")

        # create layout
        check1.grid(row=0, column=0, sticky="nswe", padx=2, pady=10, rowspan=2)
        check2.grid(row=0, column=2, sticky="nswe", padx=2, pady=10, rowspan=2)


class Menu_row_5(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        bottom_entry = ttk.Entry(self, justify="center")

        # create layout
        bottom_entry.pack(side="bottom", pady=5)


# Main frame (right mainframe)
class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        # widgets
        self.main_left = Main_left(self)
        self.main_right = Main_right(self)


class Main_left(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(side="left", expand=True, fill="both", padx=2, pady=2)

        self.create_widgets()

    def create_widgets(self):
        # widgets
        label_frame_left = ttk.Label(self, text="Label 1", background="red")
        button_frame_left = ttk.Button(self, text="Button 1")

        # layout
        label_frame_left.pack(expand=True, fill="both", padx=2, pady=2)
        button_frame_left.pack(expand=True, fill="both", padx=2, pady=2)


class Main_right(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(side="right", expand=True, fill="both", padx=2, pady=2)

        # widgets
        label_frame_right = ttk.Label(self, text="Label 2", background="blue")
        button_frame_right = ttk.Button(self, text="Button 2")

        # layout
        label_frame_right.pack(expand=True, fill="both", padx=2, pady=2)
        button_frame_right.pack(expand=True, fill="both", padx=2, pady=2)


# run
App("Test GUI", (600, 600))
