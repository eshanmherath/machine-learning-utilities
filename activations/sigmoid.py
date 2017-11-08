import numpy as np


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def derivative_sigmoid(x):
    return x * (1 - x)


values = [-1, 4, 1, -2, 0]

print(sigmoid(np.array(values)))

print(derivative_sigmoid(np.array(values)))


