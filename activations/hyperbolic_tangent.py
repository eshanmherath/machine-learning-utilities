import numpy as np


def tanh(x):
    return np.tanh(x)


def derivative_tanh(x):
    return 1.0 - np.tanh(x)**2

values = [-1, 4, 1, -2, 0]

print(tanh(np.array(values)))

print(derivative_tanh(np.array(values)))