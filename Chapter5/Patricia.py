__author__ = 'Liruo_000'


#patricia
class IntTree:
    def __init__(self, key=None, value=None):
        self.key = key
        self.left = self.right = None
        self.value = value
        self.prefix = self.mask = None

    def set_children(self, l, r):
        self.left = l
        self.right = r

    def replace_child(self, x, y):
        if self.left == x:
            self.left = y
        else:
            self.right = y

    def is_leaf(self):
        return self.left is None and self.right is None

    def get_prefix(self):
        if self.prefix is None:
            return self.key
        else:
            return self.prefix


def insert_patricia(t, key, value=None):
    if t is None:
        t = IntTree(key, value)
        return t

    node = t
    p = None

    while True:
        if match(key, node):
            p = node

            if zero(key, node.mask):
                node = node.left
            else:
                node = node.right
        else:
            if node.is_leaf() and key == node.key:
                node.value = value
            else:
                new_node = branch(node, IntTree(key, value))
                if p is None:
                    t = new_node
                else:
                    p.replace_child(node, new_node)
            break

    return t


def maskbit(x, mask):
    return x & (~(mask-1))


def match(key, tree):
    return (not tree.is_leaf()) and maskbit(key, tree.mask) == tree.prefix


def zero(k, mask):
    return k & (mask >> 1) == 0


def lcp(p1, p2):
    diff = (p1 ^ p2)
    mask = 1
    while diff != 0:
        diff >>= 1
        mask <<= 1
    return maskbit(p1, mask), mask


def branch(n1, n2):
    t = IntTree()
    (t.prefix, t.mask) = lcp(n1.get_prefix(), n2.get_prefix())
    if zero(n1.get_prefix(), t.mask):
        t.set_children(n1, n2)
    else:
        t.set_children(n2, n1)

    return t


def look_up(t, key):

    if t is None:
        return None

    while not t.is_leaf() and match(key, t):
        if zero(key, t.mask):
            t = t.left
        else:
            t = t.right

    if t.is_leaf() and t.key == key:
        return t.value
    else:
        return None

# Alphabetic Patrica
# ...

