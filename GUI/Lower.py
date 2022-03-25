import globals
import tkinter as tk

class Lower(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent, bg=globals.FRAME_COLOR, width=globals.WIDTH, height=globals.HEIGHT/6)
            self.parent = parent
            self.grid(row=6, rowspan=1, column=0)

        def num_divisions_changed():
            pass

        def type_changed():
            pass