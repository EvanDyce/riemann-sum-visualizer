from cProfile import label
from turtle import width
from matplotlib.pyplot import text
from numpy import result_type
from pyparsing import col
import globals
import tkinter as tk

class Lower(tk.Frame):
        def __init__(self, parent):
            super().__init__(parent, bg=globals.FRAME_COLOR, width=globals.WIDTH, height=globals.HEIGHT/12*3)
            self.parent = parent
            self.grid(row=6, rowspan=1, column=0)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(2, weight=1)

            self.add_widgets()


        def add_widgets(self):
            self.functions_frame_create().grid(row=0, column=0)
            self.riemann_frame_create().grid(row=0, column=1)
            self.result_frame_create().grid(row=0, column=2)


        def functions_frame_create(self):
            functions = ['Linear',
                                'Quadratic',
                                'Trinomial',
                                'Exponential',
                                'Logarithmic',
                                'sin', 
                                'cos',
                                'tan']

            functions_frame = tk.Frame(self, background=globals.FRAME_COLOR, width=globals.WIDTH/3, height=globals.HEIGHT/12*3)
            functions_frame.grid_columnconfigure(0, weight=1)
            functions_frame.grid_rowconfigure(0, weight=1)
            functions_frame.grid_rowconfigure(1, weight=1)
            functions_frame.grid_propagate(False)

            function_stringvar = tk.StringVar(functions_frame, 'Linear')
            dropdown = tk.OptionMenu(functions_frame, function_stringvar, *functions)
            dropdown.grid(row=0, column=0, sticky='nsew', padx=100, pady=50)
            dropdown.config(font=('Helvetica bold', 20), activeforeground=globals.ACCENT_COLOR)

            button = tk.Button(functions_frame, activebackground=globals.ACCENT_COLOR, text='Plot Function')
            button.grid(row=1, column=0, sticky='nsew', padx=120, pady=25)

            return functions_frame


        def riemann_frame_create(self):
            riemanns = ['Right', 
                                'Left',
                                'Middle']

            riemann_frame = tk.Frame(self, background=globals.FRAME_COLOR, width=globals.WIDTH/3, height=globals.HEIGHT/12*3)
            riemann_frame.grid_columnconfigure(0, weight=1)
            riemann_frame.grid_rowconfigure(0, weight=1)
            riemann_frame.grid_rowconfigure(1, weight=1)
            riemann_frame.grid_propagate(False)

            riemann_stringvar = tk.StringVar(riemann_frame, 'Right')
            type_dropdown = tk.OptionMenu(riemann_frame, riemann_stringvar, *riemanns)
            type_dropdown.grid(row=0, column=0, sticky='nsew', padx=100, pady=50)
            type_dropdown.config(font=('Helvetica bold', 20), activeforeground=globals.ACCENT_COLOR)

            n_slider = tk.Scale(riemann_frame, orient=tk.HORIZONTAL, label='# of subdivisions', from_=1, to=100)
            n_slider.grid(row=1, column=0, sticky='nsew', padx=120, pady=25)
            n_slider.config(font=('Helvetica bold', 12))

            return riemann_frame


        def result_frame_create(self):
            result_frame = tk.Frame(self, background=globals.FRAME_COLOR, width=globals.WIDTH/3, height=globals.HEIGHT/12*3)
            result_frame.grid_columnconfigure(0, weight=1)
            result_frame.grid_rowconfigure(0, weight=1)
            result_frame.grid_rowconfigure(1, weight=1)
            result_frame.grid_propagate(False)

            approximate_label = tk.Label(result_frame, text='Riemann Sum Area = 90')
            approximate_label.grid(row=0, column=0, sticky='nsew', padx=50, pady=25)
            approximate_label.config(font=('Helvetica bold', 20), foreground=globals.ACCENT_COLOR, background=globals.FRAME_COLOR)


            acutal_label = tk.Label(result_frame, text='Actual Area = 104')
            acutal_label.grid(row=1, column=0, sticky='nsew', padx=50, pady=25)
            acutal_label.config(font=('Helvetica bold', 20), foreground=globals.ACCENT_COLOR, background=globals.FRAME_COLOR)

            return result_frame


        


        def num_divisions_changed():
            pass

        def type_changed():
            pass