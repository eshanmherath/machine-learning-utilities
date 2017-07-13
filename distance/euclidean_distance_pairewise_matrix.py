__author__ = 'eshan'
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

instance1 = [1, 2, 3]
instance2 = [4, 5, 6]
print(euclidean_distances(np.array(instance1).reshape((len(instance1), 1)), np.array(instance2).reshape((len(instance2), 1))))

'''
    4  5  6
   ---------
1 |
2 |
3 |

'''