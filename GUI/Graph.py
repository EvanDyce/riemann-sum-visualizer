import tkinter as tk
from tracemalloc import start
from turtle import width
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.pyplot import plot_date
from functions import Functions
import numpy as np
import globals


class Graph(tk.Frame):
 
    def __init__(self, parent):
        super().__init__(master=parent, background=globals.ACCENT_COLOR, width=globals.WIDTH, height=(globals.HEIGHT/12)*8)
        self.parent = parent
        self.grid(row=2, rowspan=4, column=0)
        self.pack_propagate(False)

        self.canvas = None
        self.fig = None
        self.func_dict = {
            'Linear': Functions.Linear,
            'Quadratic': Functions.Quadratic, 
            'Cubic': Functions.Cubic,
            'Exponential': Functions.Exponential,
            'Logarithmic': Functions.Logarithm,
            'Sin': Functions.Sin,
            'Cos': Functions.Cos,
            'Tan': Functions.Tan
        }

        self.antiderivate_function = {
            'Linear': Functions.LinearAnti,
            'Quadratic': Functions.QuadraticAnti,
            'Cubic': Functions.CubicAnti,
            'Exponential': Functions.ExponentialAnti,
            'Logarithmic': Functions.LogarithmAnti,
            'Sin': Functions.SinAnti,
            'Cos': Functions.CosAnti,
            'Tan': Functions.TanAnti
        }

        self.plot('Linear', 'Right', 5)

    def clear(self, name, riemann, divisions):
        self.fig.clear(True)
        for item in self.winfo_children():
            item.destroy()

        return self.plot(name, riemann, divisions)


    def plot(self, function, riemann, divisions):
        func = self.func_dict[function]()
        domain = Functions.get_domain(func)
        fig, ax = Functions.generate(x=func[0], y=func[1], domain=domain)
        self.fig = fig

        if riemann == 'Left':
            areas = self.left_riemann(divisions, function, ax)
        elif riemann == 'Right':
            areas = self.right_riemann(divisions, function, ax)
        else:
            areas = self.midpoint_riemann(divisions, function, ax)

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=tk.YES, padx=50)
        return areas

    
    def left_riemann(self, n, function, ax: Axes):
        domain = Functions.get_domain(function)
        step = (domain[1]-domain[0])/n
        x = np.arange(start=domain[0], stop=domain[1]+0.00001, step=step)
        y = self.func_dict[function](x=x)[1]
        x_left = x[:-1]
        y_left = y[:-1]

        ax.bar(x_left,y_left,width=(domain[1]-domain[0])/n,alpha=0.2,align='edge',edgecolor='b')

        dx = (domain[1]-domain[0])/n
        approx_area = np.sum(y_left*dx)
        actual_area = self.antiderivate_function[function](domain=domain)
        return (approx_area, actual_area)

    def right_riemann(self, n, function, ax: Axes):
        domain = Functions.get_domain(function)
        step = (domain[1]-domain[0])/n
        x = np.arange(start=domain[0], stop=domain[1]+0.00001, step=step)
        y = self.func_dict[function](x=x)[1]
        x_right = x[1:]
        y_right = y[1:]

        ax.bar(x_right, y_right, width=-(domain[1]-domain[0])/n, alpha=0.2, align='edge', edgecolor='b')

        dx = (domain[1]-domain[0])/n
        approx_area = np.sum(y_right * dx)
        actual_area = self.antiderivate_function[function](domain=(domain))
        return (approx_area, actual_area)

    def midpoint_riemann(self, n, function, ax: Axes):
        domain = Functions.get_domain(function)
        step = (domain[1]-domain[0])/n
        x = np.arange(start=domain[0], stop=domain[1]+0.00001, step=step)
        x_mid = (x[1:]+x[:-1])/2
        y_mid = self.func_dict[function](x=x_mid)[1]
    

        ax.bar(x_mid, y_mid, width=(domain[1]-domain[0])/n, alpha=0.2, edgecolor='b')
        
        dx = (domain[1]-domain[0])/n
        approx_area = np.sum(y_mid*dx)

        actual_area = self.antiderivate_function[function](domain=domain)
        return (approx_area, actual_area)

