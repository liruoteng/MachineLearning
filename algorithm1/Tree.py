__author__ = 'Liruo_000'


class Node:

    def __init__(self, *k):
        if len(k) == 0:
            self.key = None
        else:
            self.key = k[0]
        self.left = None
        self.right = None
        self.parent = None


def insert(n, k):
    root = n
    parent = None
    x = Node(k)

    while n:
        parent = n
        if k < n.key:
            n = n.left
        else:
            n = n.right

    x.parent = parent
    if parent is None:
        return x
    elif k < parent.key:
        parent.left = x
    else:
        parent.right = x

    return root


def pre_order(n):
    print n.key
    if n.left:
        pre_order(n.left)
    if n.right:
        pre_order(n.right)


def in_order(n):
    if n.left:
        in_order(n.left)
    print n.key
    if n.right:
        in_order(n.right)


def post_order(n):
    if n.left:
        post_order(n.left)
    if n.right:
        post_order(n.right)
    print n.key


'''
Problem: construct BST from pre-order result and in-order result
'''


def search(n, x):
    while n and n.key != x:
        if x < n.key:
            n = n.left
        else:
            n = n.right
    return n


def find_min(n):
    if n.left:
        n = n.left
        return find_min(n)
    else:
        return n


def find_max(n):
    if n.right:
        n = n.right
        return find_max(n)
    else:
        return n


def succ(n):
    if n.right is not None:
        return find_min(n.right)
    p = n.parent
    while p is not None and p.left != n:
        n = p
        p = p.parent
    return p


def pred(n):
    if n.left is not None:
        return find_max(n.left)
    p = n.parent
    while p is not None and p.right != n:
        n = p
        p = p.parent
    return p


def delete(n, x):
    if x is None:
        return n
    root = n
    xs = x
    parent = x.parent
    if x.left is None:
        x = x.right
    elif x.right is None:
        x = x.left
    else:
        y = find_min(x.right)
        x.key = y.key
        if y.parent != x:
            y.parent.left = y.right
        else:
            x.right = y.right
        return root
    if x is not None:
        x.parent = None

    if parent is None:
        root = x
    else:
        if parent.left == xs:
            parent.left = x
        else:
            parent.right = x

    return root


def delete2(n, x):
    if x is None:
        return n

    root = n
    xs = x
    parent = x.parent

    if x.left is None:
        x = x.right
    elif x.right is None:
        x = x.left
    else:
        y = find_max(x.left)
        x.key = y.key
        if y.parent != x:
            y.parent.right = y.left
        else:
            x.left = y.left

        return root

    if parent is None:
        root = x
    else:
        if parent.left == xs:
            parent.left = x
        else:
            parent.right = x

    return root





