import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.pyplot import plot_date
from functions import Functions
import globals


class Graph(tk.Frame):
 
    def __init__(self, parent):
        super().__init__(master=parent, background=globals.ACCENT_COLOR, width=globals.WIDTH, height=(globals.HEIGHT/12)*8)
        self.parent = parent
        self.grid(row=2, rowspan=4, column=0)
        self.pack_propagate(False)

        self.canvas = None
        self.fig = None
        self.plot('Linear')

    def clear(self, name):
        print('cleared')
        self.fig.clear(True)
        for item in self.winfo_children():
            item.destroy()

        self.plot(name)


    def plot(self, function):
        func_dict = {
            'Linear': Functions.Linear,
            'Quadratic': Functions.Quadratic, 
            'Cubic': Functions.Cubic,
            'Exponential': Functions.Exponential,
            'Logarithmic': Functions.Logarithm,
            'Sin': Functions.Sin,
            'Cos': Functions.Cos,
            'Tan': Functions.Tan
        }

        fig = func_dict[function]()
        self.fig = fig
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES, padx=50)
