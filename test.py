__author__ = 'Liruo_000'

import numpy as np
import operator

array5 = np.linspace(0, 10, 11)
array1 = np.logspace(0, 10, num=10, base=2.0)


#y = np.zeros((3,4))

#print y

#z = y.shape
#print z

#x = y.shape[0]
#print x
dic = {"label": 3, "mydic": 4}

sortdic = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)
#cube = np.zeros((2, 3)).astype(np.int16) + 1.1

#print cube[1, :]
print sortdic[0][0]



