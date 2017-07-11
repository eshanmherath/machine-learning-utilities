__author__ = 'eshan'

########################################################################################################################

from math import sqrt                                                         # using pure python


def euclidean_distance_method1(example1, example2):
    return sqrt(sum((e1 - e2) ** 2 for e1, e2 in zip(example1, example2)))

print(euclidean_distance_method1([1, 2, 3], [4, 5, 6]))

########################################################################################################################

import numpy as np                                                            # using numpy


def euclidean_distance_method2(example1, example2):
    return np.linalg.norm(np.array(example1) - np.array(example2))

print(euclidean_distance_method2([1, 2, 3], [4, 5, 6]))

########################################################################################################################

from scipy.spatial import distance                                            # using scipy


def euclidean_distance_method3(example1, example2):
    return distance.euclidean(example1, example2)

print(euclidean_distance_method3([1, 2, 3], [4, 5, 6]))

########################################################################################################################