# Imports
import numpy as np
from functions2d.function2d import Function2D


# Problem
class Trid(Function2D):
    """ Trid Function. """

    def __init__(self):
        """ Constructor. """
        self.min = np.array([0.0, 0.0])
        self.value = 0.0
        self.domain = np.array([[-4, 4], [-4, 4]])
        self.smooth = True
        self.info = [True, False, False]
        self.latex_name = "Trid Function"
        self.latex_type = "Bowl-Shaped"
        self.latex_cost = "\[ f(x,y) = ... \]"
        self.latex_desc = "The Trid function has no local minimum except the global one. It is shown here in its" \
                          "two-dimensional form. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = np.sum([(x[i]-1)**2 for i in range(0, 2)]) - np.sum([x[i]*x[i-1] for i in range(1, 2)])
        # Return Cost
        return c