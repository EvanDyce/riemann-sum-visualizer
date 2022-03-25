import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import globals

class Graph(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent, background=globals.ACCENT_COLOR, width=globals.WIDTH, height=(globals.HEIGHT/12)*8)
        self.parent = parent
        self.grid(row=2, rowspan=4, column=0)
        self.pack_propagate(False)
        
        self.plot()

    def plot(self):
        fig = Figure(dpi=100)
        y = [i**2 for i in range(101)]
        plot1 = fig.add_subplot(111)
        plot1.plot(y)

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
   
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES, padx=50)

        # toolbar = NavigationToolbar2Tk(canvas, self)
        # toolbar.update()
        # toolbar.get_tk_widget().grid()
