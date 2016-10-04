__author__ = 'Liruo_000'

'''Number Puzzle Problem'''
def get_number(n):
    x = 1
    i = 0
    while True:
        if valid(x):
            i += 1
            if i == n:
                return x
        x += 1


def valid(num):
    while num % 2 == 0:
        num /= 2
    while num % 3 == 0:
        num /= 3
    while num % 5 == 0:
        num /= 5

    if num == 1:
        return True
    else:
        return False

