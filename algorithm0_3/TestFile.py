__author__ = 'Liruo_000'
import time
import algorithm0_3.QueueSolution
import algorithm0_3.MultiQueue

'''
# Brute Force implementation
start = time.clock()
result = algorithm0_3.BruteForce.get_number(1500)
end = time.clock()
print result, (end - start), "s"
'''
# Queue implementation
start = time.clock()

result = algorithm0_3.QueueSolution.get_number(1500)
end = time.clock()
print result, (end - start), "s"

# Queue implementation
start = time.clock()

result = algorithm0_3.MultiQueue.get_number(1500)
end = time.clock()
print result, (end - start), "s"


