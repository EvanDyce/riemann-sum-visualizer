import tkinter as tk
from turtle import back, width
import globals

class Upper(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent, bg=globals.FRAME_COLOR, width=globals.WIDTH, height=globals.HEIGHT/6)
            self.parent = parent
            self.grid(row=1, rowspan=1, column=0)
            self.grid_rowconfigure(1, weight=1)
            self.grid_rowconfigure(2, weight=1)
            self.grid_propagate(False)

            self.add_widgets()

        def add_widgets(self):
            # Creating a frame to contain the label and input of the function
            function_frame = tk.Frame(self, background=globals.GRAPH_COLOR, height=(globals.HEIGHT/6)/3, width=globals.WIDTH)
            function_frame.grid_propagate(False)
            function_frame.columnconfigure(1, weight=1)
            function_frame.columnconfigure(2, weight=2)
            function_frame.rowconfigure(1, weight=1)

            # Creating the label for the function
            function_label = tk.Label(function_frame, text='Function', foreground=globals.ACCENT_COLOR)
            function_label.grid(row=1, column=1, columnspan=1, sticky='nsew')
            function_label.config(font=('Helvatical bold', 25))

            # Adding the text input for the function
            function_input = tk.Text(function_frame, background=globals.GRAPH_COLOR, height=1)
            function_input.grid(row=1, column=2, padx=23, sticky='ew')

            function_frame.grid(row=1, column=1, padx=20)

            # Label that is going to show the latex formatted text hopefully
            latex_label = tk.Label(self, text='Hello this is the thing that I am writing right now', foreground=globals.ACCENT_COLOR, background='#ff0000')
            latex_label.config(font=('Helvetica bold', 25))
            latex_label.grid(row=2, column=1, sticky='nsew',  pady=20, padx=20)

            # Plot button put at the bottom of the thing
            plot_button = tk.Button(self, background=globals.ACCENT_COLOR, height=1, width=8, text="Plot")
            plot_button.grid(row=3, column=1)


        def latex():
            pass