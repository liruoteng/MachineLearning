__author__ = 'Liruo_000'
import kNN
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

dating_data_matrix, dating_label = kNN.file2matrix('datingTestSet.txt')
fig = plt.figure()

ax = fig.add_subplot(111)
ax.scatter(dating_data_matrix[:, 1], dating_data_matrix[:, 2])

# Example 2
# this example fails because it can't convert ndarray to flaot now
#ax.scatter(dating_data_matrix[:, 1], dating_data_matrix[:, 2], 15.0*array(dating_label), 15.0*array(dating_label))

plt.show()

#Example 3
# normalize numeric values


