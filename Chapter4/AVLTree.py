__author__ = 'Liruo_000'


class Node:

    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None
        self.parent = None
        self.delta = None


def avl_insertion(t, key):
    root = t
    x = Node(key)
    p = None

    while t:
        p = t
        if key < t.key:
            t = t.left
        else:
            t = t.right

    if p is None:
        root = x
    elif key < p.key:
        p.left = x
    else:
        p.right = x

    return avl_insert_fix(root, x)


def avl_insert_fix(t, x):
    while x.parent is not None:
        d2 = d1 = x.parent.delta
        if x == x.parent.left:
            d2 -= 1
        else:
            d2 += 1
        x.parent.delta = d2

        (p, l, r) = (x.parent, x.parent.left, x.parent.right)
        if abs(d1) == 1 and abs(d2) == 0:
            return t
        elif abs(d1) == 0 and abs(d2) == -1:
            x = x.parent
        elif abs(d1) == 1 and abs(d2) == 2:
            if d2 == 2:
                if r.delta == 1:
                    p.delta = 0
                    r.delta = 0
                    t = left_rotate(t, p)
                if r.delta == -1:
                    dy = r.left.delta
                    if dy == 1:
                        p.delta = -1
                    else:
                        p.delta = 0
                    r.left.delta = 0
                    if dy == -1:
                        r.delta = 0
                    t = right_rotate(t, r)
                    t = left_rotate(t, p)
            if d2 == -2:
                if l.delta == -1:
                    p.delta = 0
                    l.delta = 0
                    t = right_rotate(t, p)
                if l.delta == 1:
                    dy = l.right.delta
                    if dy == 1:
                        l.delta = -1
                    else:
                        l.delta = 0
                    l.right.delta = 0
                    if dy = -1:
                        p.delta = 1
                    else:
                        p.delta = 0
                    t = left_rotate(t, l)
                    t = right_rotate(t.p)
        break
    return t
