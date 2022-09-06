import matplotlib.pyplot as plt
import numpy as np
from datetime import date

class Generator():

    def __init__(self, f):
        self.ifs = f

    def generate_instance(self, no_iter):


class DeJongIFS():

    def __init__(self, a, b, c, d, p_o, no_iter, name):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.p_o = p_o
        self.no_iter = no_iter
        self.name = name

class OriginalDeJong(DeJongIFS):

    def __init__(self, a, b, c, d, p_o, no_iter):
        super().__init__(self, a, b, c, d, p_o, no_iter, 'Original DeJong')

    def

def de_jong_ifs(a, b, c, d, p_o, no_iter=5):
    """ Function that generates points using the De Jong IFS

    """
    # create empty arrays
    x = np.zeros(no_iter)
    y = np.zeros(no_iter)

    # include starting point
    x[0], y[0] = p_o[0], p_o[1]

    # iterate to create all points using the De Jong IFS
    for i in np.arange(1, no_iter):
        # x[i] = np.sin(np.deg2rad(a*y[i-1])) - np.cos(np.deg2rad(b*x[i-1]))
        # y[i] = np.sin(np.deg2rad(c*x[i-1])) - np.cos(np.deg2rad(d*y[i-1]))

        # cool ones

        # style 0
        # x[i] = np.sin(a*y[i-1]) - np.cos(b*x[i-1])
        # y[i] = np.sin(c*x[i-1]) - np.cos(d*y[i-1])

        # style 1
        # x[i] = np.sin(a*y[i-1]**3) * np.cos(b*x[i-1]**2)
        # y[i] = np.sin(c*x[i-1]) - np.cos(d*y[i-1])

        # style 2
        # x[i] = np.sin(a*y[i-1]**3) - np.cos(b*x[i-1]**2)
        # y[i] = np.sin(c*x[i-1]) - np.cos(d*y[i-1])

        # style 3
        # x[i] = np.sin(a*y[i-1])**3 - np.cos(b*x[i-1])
        # y[i] = np.sin(c*x[i-1]) - np.cos(d*y[i-1])

        #  style 4
        # x[i] = np.sin(a*y[i-1])**3 * np.cos(b*x[i-1])
        # y[i] = np.sin(c*x[i-1]) - 1.3*np.cos(d*y[i-1])

        # style 5
        x[i] = np.sin(a * y[i - 1] ** 2) * np.cos(b * x[i - 1]) ** 2
        y[i] = np.sin(c * x[i - 1]) - 5 * np.cos(d * y[i - 1] ** 2)

        # style 6
        # x[i] = np.sin(a*y[i-1]**3) * np.cos(b*x[i-1])**2
        # y[i] = np.sin(c*x[i-1]) - 2*np.cos(d*y[i-1]**2)

        # style 7
        # x[i] = np.sin(a*y[i-1]**3) - np.cos(b*x[i-1])**3
        # y[i] = np.sin(c*x[i-1]) * 2*np.cos(d*y[i-1]**2)

        # style 8
        # x[i] = np.sin(a*y[i-1]**3) * np.cos(b*x[i-1])**3
        # y[i] = np.sin(c*x[i-1]*y[i-1]) - 3*np.cos(d*y[i-1]**2)

        # style 9
        # x[i] = np.sin(a*y[i-1]) - np.cos(b*x[i-1])
        # y[i] = np.sin(c*x[i-1]*y[i-1]**2) - 3*np.cos(d*y[i-1])

        # style 10
        # x[i] = np.sin(a*y[i-1]) - np.cos(b*x[i-1])
        # y[i] = np.sin(c*x[i-1]*y[i-1]**5) - 3*np.cos(d*y[i-1])

        # i] = np.sin(a*y[i-1])**3 * np.cos(b*x[i-1])
        # y[i] = np.sin(c*x[i-1]) - 1.3*np.cos(d*y[i-1])

    return x, y
