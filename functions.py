from math import cos, log, sin, tan
from scipy.integrate import quad        
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

    @staticmethod
    def Linear(x=np.linspace(-5, 5, 200)):
        y = x
        return (x, y)

    @staticmethod
    def LinearAnti(domain=(-5, 5)):
        answer = quad(lambda x: x, domain[0], domain[1])
        return answer[0]
        

    @staticmethod
    def Quadratic(x=np.linspace(-5, 5, 200)):
        y = x**2
        return (x, y)

    @staticmethod
    def QuadraticAnti(domain=(-5, 5)):
        answer = quad(lambda x: x**2, domain[0], domain[1])
        return answer[0]


    @staticmethod
    def Cubic(x=np.linspace(-5, 5, 200)):
        y = x**3
        return (x, y)

    @staticmethod
    def CubicAnti(domain=(-5, 5)):
        answer = quad(lambda x: x**3, domain[0], domain[1])
        return answer[0]


    @staticmethod
    def Exponential(x=np.linspace(-1, 5, 200)):
        y = 2**x
        return (x, y)

    @staticmethod
    def ExponentialAnti(domain=(-1, 5)):
        answer = quad(lambda x: 2**x, domain[0], domain[1])
        return answer[0]

    @staticmethod
    def Logarithm(x=np.linspace(0.001, 5, 200)):
        y = np.array([log(num) for num in x])
        return (x, y)

    @staticmethod
    def LogarithmAnti(domain=(0.001, 5)):
        answer = quad(lambda x: log(x), domain[0], domain[1])
        return answer[0]

    @staticmethod
    def Sin(x=np.linspace(-5, 5, 200)):
        y = np.array([sin(num) for num in x])
        return (x, y)

    @staticmethod
    def SinAnti(domain=(-5, 5)):
        answer = quad(lambda x: sin(x), domain[0], domain[1])
        return answer[0]

    @staticmethod
    def Cos(x=np.linspace(-5, 5, 200)):
        y = np.array([cos(num) for num in x])
        return (x, y)

    @staticmethod
    def CosAnti(domain=(-5, 5)):
        answer = quad(lambda x: cos(x), domain[0], domain[1])
        return answer[0]

    @staticmethod
    def Tan(x=np.linspace(-5, 5, 200)):
        y = np.array([tan(num) for num in x])
        return (x, y)

    @staticmethod
    def TanAnti(domain=(-5, 5)):
        answer = quad(lambda x: tan(x), domain[0], domain[1])
        return answer[0]
