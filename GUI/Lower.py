from GUI.Graph import Graph
import globals
import tkinter as tk
from functions import Functions

class Lower(tk.Frame):
        def __init__(self, parent, graph: Graph):
            super().__init__(parent, bg=globals.FRAME_COLOR, width=globals.WIDTH, height=globals.HEIGHT/12*3)
            self.parent = parent
            self.grid(row=6, rowspan=1, column=0)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=1)
            self.grid_columnconfigure(2, weight=1)

            self.graph = graph
            self.divisions = 5
            self.function = 'Linear'
            self.riemann = 'Right'
            self.add_widgets()


        def add_widgets(self):
            self.functions_frame_create().grid(row=0, column=0)
            self.riemann_frame_create().grid(row=0, column=1)
            self.result_frame_create().grid(row=0, column=2)

        def func_changed(self, name, index, mode):
            func = self.getvar(name)
            self.function = func
            self.graph.clear(func, self.riemann, self.divisions)


        def functions_frame_create(self):
            functions = ['Linear',
                                'Quadratic',
                                'Cubic',
                                'Exponential',
                                'Logarithmic',
                                'Sin', 
                                'Cos',
                                'Tan']

            functions_frame = tk.Frame(self, background=globals.FRAME_COLOR, width=globals.WIDTH/3, height=globals.HEIGHT/12*3)
            functions_frame.grid_columnconfigure(0, weight=1)
            functions_frame.grid_rowconfigure(0, weight=1)
            functions_frame.grid_rowconfigure(1, weight=1)
            functions_frame.grid_propagate(False)

            function_stringvar = tk.StringVar(functions_frame, 'Linear', name='function')
            dropdown = tk.OptionMenu(functions_frame, function_stringvar, *functions)
            dropdown.grid(row=0, column=0, sticky='nsew', padx=100, pady=50)
            dropdown.config(font=('Helvetica bold', 20), activeforeground=globals.ACCENT_COLOR)
            function_stringvar.trace('w', self.func_changed)

            return functions_frame

        def riemann_changed(self, name, index, mode):
            self.riemann = self.getvar(name)
            approx, actual = self.graph.clear(self.function, self.riemann, self.divisions)
            self.setvar(name='approx_riemann', value=f'Riemann Sum Area = {round(approx, 4)}')
            self.setvar(name='actual_riemann', value=f'Actual Area = {round(actual, 4)}')

        def num_divisions_changed(self, name):
            self.divisions = int(self.getvar(name='divisions'))
            approx, actual = self.graph.clear(self.function, self.riemann, self.divisions)
            self.setvar(name='approx_riemann', value=f'Riemann Sum Area = {round(approx, 4)}')
            self.setvar(name='actual_riemann', value=f'Actual Area = {round(actual, 4)}')

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
            riemann_stringvar.trace('w', self.riemann_changed)

            divsions_var = tk.IntVar(self, 5, name='divisions')
            n_slider = tk.Scale(riemann_frame, orient=tk.HORIZONTAL, label='# of subdivisions', from_=1, to=100, variable=divsions_var)
            n_slider.grid(row=1, column=0, sticky='nsew', padx=120, pady=25)
            n_slider.config(font=('Helvetica bold', 12))
            n_slider.bind('<ButtonRelease-1>', self.num_divisions_changed)

            return riemann_frame


        def result_frame_create(self):
            result_frame = tk.Frame(self, background=globals.FRAME_COLOR, width=globals.WIDTH/3, height=globals.HEIGHT/12*3)
            result_frame.grid_columnconfigure(0, weight=1)
            result_frame.grid_rowconfigure(0, weight=1)
            result_frame.grid_rowconfigure(1, weight=1)
            result_frame.grid_propagate(False)

            approximat_var = tk.StringVar(self, value='Riemann Sum Area = 10', name='approx_riemann')
            approximate_label = tk.Label(result_frame, textvariable=approximat_var)
            approximate_label.grid(row=0, column=0, sticky='nsew', padx=50, pady=25)
            approximate_label.config(font=('Helvetica bold', 20), foreground=globals.ACCENT_COLOR, background=globals.FRAME_COLOR)

            
            actual_var = tk.StringVar(self, value='Actual Area = 0', name='actual_riemann')
            actual_label = tk.Label(result_frame, textvariable=actual_var)
            actual_label.grid(row=1, column=0, sticky='nsew', padx=50, pady=25)
            actual_label.config(font=('Helvetica bold', 20), foreground=globals.ACCENT_COLOR, background=globals.FRAME_COLOR)

            return result_frame


