# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class Bohachevsky3(Function2D):
    """ Bohachevsky No. 3 Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-np.inf, np.inf], [-np.inf, np.inf]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Bohachevsky No. 3 Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "..."

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = x[0]**2 + 2*x[1]**2 - 0.3*np.cos(3*np.pi*x[0] + 4*np.pi*x[1]) + 0.3
        # Return Cost
        return c