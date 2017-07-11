__author__ = 'eshan'

########################################################################################################################

import csv                                                                              # using pure python

with open('csv/iris_training.csv', 'r') as f:
    lines = csv.reader(f)
    for row in lines:
        print(', '.join(row))


########################################################################################################################

import pandas as pd                                                                     # using pandas

df = pd.read_csv('csv/iris_training.csv')
print(df)