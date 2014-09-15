# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class Rastrigin(Function2D):
    """ Rastrigin Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-5.12, 5.12], [-5.12, 5.12]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Rastrigin Function"
        self.latex_type = "Many Local Minima"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The Rastrigin function has several local minima. It is highly multimodal, but locations of the minima are regularly distributed."

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = 20 + (x[0]**2 - 10*np.cos(2*np.pi*x[0])) + (x[1]**2 - 10*np.cos(2*np.pi*x[1]))
        # Return Cost
        return c