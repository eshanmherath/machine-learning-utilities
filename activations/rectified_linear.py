import numpy as np


def relu(x):
    x[x < 0] = 0
    return x


def derivative_relu(x):
    x[x <= 0] = 0
    x[x > 0] = 1
    return x

values = [-1, 4, 1, -2, 0]

print(relu(np.array(values)))

print(derivative_relu(np.array(values)))