import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from GUI import Graph, Lower, Upper
import globals


class app(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self)
        self.parent = parent
        self.title('Riemann Sums')
        self.geometry(f'{globals.WIDTH}x{globals.HEIGHT}')
        self.upper = Upper.Upper(self)
        self.graph = Graph.Graph(self)
        self.lower = Lower.Lower(self, graph=self.graph)
        

if __name__ == "__main__":
    app = app(None)
    
    app.mainloop()
    