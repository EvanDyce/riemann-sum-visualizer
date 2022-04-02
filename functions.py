from math import cos, log, sin, tan
import matplotlib.figure as plt
from matplotlib.backends.backend_tkagg import (NavigationToolbar2Tk, FigureCanvasTkAgg)
import numpy as np


class Functions():

    @staticmethod
    def get_domain(function):
        if function == 'Exponential':
            return (-1, 5)
        elif function == 'Logarithmic':
            return (0.001, 5)
        else:
            return (-5, 5)

        
    @staticmethod
    def generate(x, y, domain): 
        fig = plt.Figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.hlines(y=0, color='r', xmin=domain[0], xmax=domain[1])
        ax.plot(x, y)
        
        return (fig, ax)

    # @staticmethod
    # def left_riemann(n, function, fig):
    #     domain = Functions.get_domain(function)

    #     x = np.linspace(domain[0], domain[1], n)
    #     y = self.func_dict[function](x=x)[1]
    #     x_left = x[:-1]
    #     y_left = y[:-1]
    #     ax = fig.add_subplot(1, 1, 1, sharex=fig.get_axes()[0], sharey=fig.get_axes()[0])

    #     ax.bar(x_left,y_left,width=(domain[1]-domain[0])/n,alpha=0.2,align='edge',edgecolor='b')

    @staticmethod
    def Linear(x=np.linspace(-5, 5, 200)):
        y = x
        return (x, y)

    @staticmethod
    def Quadratic(x=np.linspace(-5, 5, 200)):
        y = x**2
        return (x, y)

    @staticmethod
    def Cubic(x=np.linspace(-5, 5, 200)):
        y = x**3
        return (x, y)

    @staticmethod
    def Exponential(x=np.linspace(-1, 5, 200)):
        y = 2**x
        return (x, y)

    @staticmethod
    def Logarithm(x=np.linspace(0.001, 5, 200)):
        y = [log(num) for num in x]
        return (x, y)

    @staticmethod
    def Sin(x=np.linspace(-5, 5, 200)):
        y = [sin(num) for num in x]
        return (x, y)

    @staticmethod
    def Cos(x=np.linspace(-5, 5, 200)):
        y = [cos(num) for num in x]
        return (x, y)

    @staticmethod
    def Tan(x=np.linspace(-5, 5, 200)):
        y = [tan(num) for num in x]
        return (x, y)

