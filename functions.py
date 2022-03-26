from math import cos, log, sin, tan
import matplotlib.figure as plt
from matplotlib.backends.backend_tkagg import (NavigationToolbar2Tk, FigureCanvasTkAgg)
import numpy as np


class Functions():
    @staticmethod
    def generate(x, y, domain):
        fig = plt.Figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.hlines(y=0, color='r', xmin=domain[0], xmax=domain[1])
        ax.plot(x, y)
        return fig


    @staticmethod
    def Linear():
        x = np.linspace(-10, 10, 200)
        y = x
        return Functions.generate(x, y, (-10, 10))

    @staticmethod
    def Quadratic():
        x = np.linspace(-10, 10, 200)
        y = x**2
        return Functions.generate(x, y, (-10, 10))

    @staticmethod
    def Cubic():
        x = np.linspace(-10, 10, 200)
        y = x**3
        return Functions.generate(x, y, (-10, 10))

    @staticmethod
    def Exponential():
        x = np.linspace(-1, 10, 200)
        y = 2**x
        return Functions.generate(x, y, (-1, 10))

    @staticmethod
    def Logarithm():
        x = np.linspace(0.001, 15, 200)
        y = [log(num) for num in x]
        return Functions.generate(x, y, (0, 15))

    @staticmethod
    def Sin():
        x = np.linspace(-10, 10, 200)
        y = [sin(num) for num in x]
        return Functions.generate(x, y, (-10, 10))

    @staticmethod
    def Cos():
        x = np.linspace(-10, 10, 200)
        y = [cos(num) for num in x]
        return Functions.generate(x, y, (-10, 10))

    @staticmethod
    def Tan():
        x = np.linspace(-10, 10, 200)
        y = [tan(num) for num in x]
        return Functions.generate(x, y, (-10, 10))