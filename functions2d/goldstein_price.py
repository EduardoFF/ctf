# Imports
import numpy as np
from numpy import exp, cos, sin, sqrt, pi
from functions2d.function2d import Function2D


# Problem
class GoldsteinPrice(Function2D):
    """ Goldstein-Price Function. """

    def __init__(self):
        """ Constructor. """
        # Information
        self.min = np.array([0.0, -1.0])
        self.value = 3.0
        self.domain = np.array([[-2.0, 2.0], [-2.0, 2.0]])
        self.n = 2
        self.smooth = True
        self.info = [True, True, True]
        # Description
        self.latex_name = "Goldstein-Price"
        self.latex_type = "Other"
        self.latex_cost = r"\[ f(\mathbf{x}) = [(2x_0 - 3x_1)^2(12x_0^2 - 36x_0x_1 - 32x_0 + 27x_1^2 + 48x_1 + 18) + 30] \times [(x_0 + x_1 + 1)^2(3x_0^2 + 6x_0x_1 - 14x_0 + 3x_1^2 - 14x_1 + 19) + 1] \]"
        self.latex_desc = "The Goldstein-Price function has several local minima. "

    def cost(self, x):
        """ Cost function. """
        # Cost
        c = np.zeros(x.shape[1:])
        # Calculate Cost
        c = ((2*x[0] - 3*x[1])**2*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + 30)*((x[0] + x[1] + 1)**2*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19) + 1)
        # Return Cost
        return c

    def grad(self, x):
        """ Grad function. """
        # Grad
        g = np.zeros(x.shape)
        # Calculate Grads
        g[0] = ((2*x[0] - 3*x[1])**2*(24*x[0] - 36*x[1] - 32) + (8*x[0] - 12*x[1])*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18))*((x[0] + x[1] + 1)**2*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19) + 1) + ((2*x[0] - 3*x[1])**2*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + 30)*((x[0] + x[1] + 1)**2*(6*x[0] + 6*x[1] - 14) + (2*x[0] + 2*x[1] + 2)*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19))
        g[1] = ((-12*x[0] + 18*x[1])*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + (2*x[0] - 3*x[1])**2*(-36*x[0] + 54*x[1] + 48))*((x[0] + x[1] + 1)**2*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19) + 1) + ((2*x[0] - 3*x[1])**2*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + 30)*((x[0] + x[1] + 1)**2*(6*x[0] + 6*x[1] - 14) + (2*x[0] + 2*x[1] + 2)*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19))
        # Return Grad
        return g

    def hess(self, x):
        """ Hess function. """
        # Hess
        h = np.zeros((2, 2) + x.shape[1:])
        # Calculate Hess
        h[0][0] = 2*((2*x[0] - 3*x[1])**2*(24*x[0] - 36*x[1] - 32) + (8*x[0] - 12*x[1])*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18))*((x[0] + x[1] + 1)**2*(6*x[0] + 6*x[1] - 14) + (2*x[0] + 2*x[1] + 2)*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19)) + ((2*x[0] - 3*x[1])**2*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + 30)*(6*x[0]**2 + 12*x[0]*x[1] - 28*x[0] + 6*x[1]**2 - 28*x[1] + 6*(x[0] + x[1] + 1)**2 + 2*(2*x[0] + 2*x[1] + 2)*(6*x[0] + 6*x[1] - 14) + 38) + ((x[0] + x[1] + 1)**2*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19) + 1)*(96*x[0]**2 - 288*x[0]*x[1] - 256*x[0] + 216*x[1]**2 + 384*x[1] + 24*(2*x[0] - 3*x[1])**2 + 2*(8*x[0] - 12*x[1])*(24*x[0] - 36*x[1] - 32) + 144)
        h[0][1] = ((-12*x[0] + 18*x[1])*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + (2*x[0] - 3*x[1])**2*(-36*x[0] + 54*x[1] + 48))*((x[0] + x[1] + 1)**2*(6*x[0] + 6*x[1] - 14) + (2*x[0] + 2*x[1] + 2)*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19)) + ((2*x[0] - 3*x[1])**2*(24*x[0] - 36*x[1] - 32) + (8*x[0] - 12*x[1])*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18))*((x[0] + x[1] + 1)**2*(6*x[0] + 6*x[1] - 14) + (2*x[0] + 2*x[1] + 2)*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19)) + ((2*x[0] - 3*x[1])**2*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + 30)*(6*x[0]**2 + 12*x[0]*x[1] - 28*x[0] + 6*x[1]**2 - 28*x[1] + 6*(x[0] + x[1] + 1)**2 + 2*(2*x[0] + 2*x[1] + 2)*(6*x[0] + 6*x[1] - 14) + 38) + ((x[0] + x[1] + 1)**2*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19) + 1)*(-144*x[0]**2 + 432*x[0]*x[1] + 384*x[0] - 324*x[1]**2 - 576*x[1] + (-12*x[0] + 18*x[1])*(24*x[0] - 36*x[1] - 32) - 36*(2*x[0] - 3*x[1])**2 + (8*x[0] - 12*x[1])*(-36*x[0] + 54*x[1] + 48) - 216)
        h[1][0] = h[0][1]
        h[1][1] = 2*((-12*x[0] + 18*x[1])*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + (2*x[0] - 3*x[1])**2*(-36*x[0] + 54*x[1] + 48))*((x[0] + x[1] + 1)**2*(6*x[0] + 6*x[1] - 14) + (2*x[0] + 2*x[1] + 2)*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19)) + ((2*x[0] - 3*x[1])**2*(12*x[0]**2 - 36*x[0]*x[1] - 32*x[0] + 27*x[1]**2 + 48*x[1] + 18) + 30)*(6*x[0]**2 + 12*x[0]*x[1] - 28*x[0] + 6*x[1]**2 - 28*x[1] + 6*(x[0] + x[1] + 1)**2 + 2*(2*x[0] + 2*x[1] + 2)*(6*x[0] + 6*x[1] - 14) + 38) + ((x[0] + x[1] + 1)**2*(3*x[0]**2 + 6*x[0]*x[1] - 14*x[0] + 3*x[1]**2 - 14*x[1] + 19) + 1)*(216*x[0]**2 - 648*x[0]*x[1] - 576*x[0] + 486*x[1]**2 + 864*x[1] + 2*(-12*x[0] + 18*x[1])*(-36*x[0] + 54*x[1] + 48) + 54*(2*x[0] - 3*x[1])**2 + 324)
        # Return Hess
        return h