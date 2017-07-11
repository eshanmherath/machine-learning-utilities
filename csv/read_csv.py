__author__ = 'eshan'

########################################################################################################################

import csv                                                                           # using pure python

with open('iris_training.csv', 'r') as f:
    lines = csv.reader(f)
    for row in lines:
        print(', '.join(row))


########################################################################################################################

import pandas as pd                                                                  # using pandas

df = pd.read_csv('iris_training.csv')
print(df)


########################################################################################################################

import os                                                                            # using pandas with path validation
import pandas as pd

if os.path.exists('iris_training.csv'):
    df = pd.read_csv('iris_training.csv', index_col=0)
print(df)


########################################################################################################################