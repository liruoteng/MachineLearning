__author__ = 'Liruo_000'

#integer Trie
class IntTrie:
    def __init__(self):
        self.value = None
        self.left = self.right = None


def trie_insert(t, key, value=None):
    if t is None:
        t = IntTrie()
    p = t
    while key != 0:
        if key & 1  == 0:
            if p.left is None:
                p.left = IntTrie()
                p = p.left
        else:
            if p.right is None:
                p.right = IntTrie()
            p = p.right
        key >>= 1
    p.value = value

    return t


def lookup(t, key):
    while key != 0 and (t is not None):
        if key & 1 == 0:
            t = t.left
        else:
            t = t.right

        key >>= 1

    if t is not None:
        return t.value
    else:
        return None


# Alphabetic Trie
# ...