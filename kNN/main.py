__author__ = 'Liruo_000'
import kNN
#from numpy import *
import matplotlib
import matplotlib.pyplot as plt

# example 2.2.1
# read matrix and labels(targes) from files
# dating_data_matrix, dating_label = kNN.file2matrix('datingTestSet.txt')

# Example 2.2.2
# this example fails because it can't convert ndarray to flaot now
#ax.scatter(dating_data_matrix[:, 1], dating_data_matrix[:, 2], 15.0*array(dating_label), 15.0*array(dating_label))

#Example 2.2.3
# normalize numeric values
# norm_matrix, ranges, min_value = kNN.auto_norm(dating_data_matrix)

# create plot
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(norm_matrix[:, 1], norm_matrix[:, 2])
#plt.show()

# example 2.2.4
# error rate

# kNN.dating_class_test()

# 2.2.5 putting together
kNN.classify_person()


