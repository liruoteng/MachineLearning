__author__ = 'Liruo_000'
import time
'''Improvement using queue method'''


def get_number(n):
    queue = [1]
    x = 0
    while n > 0:
        x = queue.pop(0)
        enqueue(queue, 2*x)
        enqueue(queue, 3*x)
        enqueue(queue, 5*x)
        n -= 1

    return x


def enqueue(queue, x):
    i = 0
    while i < len(queue) and queue[i] < x:
        i += 1
    if i < len(queue) and x == queue[i]:
        return
    queue.insert(i, x)



