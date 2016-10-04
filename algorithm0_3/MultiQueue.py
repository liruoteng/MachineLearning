__author__ = 'Liruo_000'
'''Chapter 0.3: improvements 2'''


def get_number(n):
    if n == 1:
        return 1
    else:
        x = 0
        q2 = [2]
        q3 = [3]
        q5 = [5]

        while n > 1:
            x = get_minimum(q2, q3, q5)

            if x == q2[0]:
                q2.remove(x)
                q2.append(2*x)
                q3.append(3*x)
                q5.append(5*x)
            elif x == q3[0]:
                q3.remove(x)
                q3.append(3*x)
                q5.append(5*x)
            else:
                q5.remove(x)
                q5.append(5*x)
            n -= 1
        return x


def get_minimum(q2, q3, q5):

    if q2[0] <= q3[0]:
        if q2[0] <= q5[0]:
            return q2[0]
        else:
            return q5[0]
    else:
        if q3[0] <= q5[0]:
            return q3[0]
        else:
            return q5[0]