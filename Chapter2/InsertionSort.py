__author__ = 'uidw5235'
'''Insertion Sort function library'''
''' Chapter 2 '''


# ==========================================================
# def isort(args) : plain insertion sort
# ==========================================================
def isort(xs):
    n = len(xs)
    for i in range(1, n):
        x = xs[i]
        j = i-1
        while j >= 0 and xs[j] > x:
            xs[j+1] = xs[j]
            j -= 1
        xs[j+1] = x
# ==========================================================


# ==========================================================
#  def bs_sort(args): Insertion sort with binary search find
# ==========================================================
def bs_sort(xs):
    n = len(xs)
    for i in range(1, n):
        x = xs[i]
        p = binary_search(xs[:i], x)
        for j in range(i, p, -1):
            xs[j] = xs[j-1]
        xs[p] = x


# Binary Search in Find step
def binary_search(A, x):
    lowerbound = 0
    upperbound = len(A)
    while lowerbound < upperbound:
        middle = (lowerbound + upperbound) / 2
        if x == A[middle]:
            return middle
        elif x > A[middle]:
            lowerbound = middle + 1
        else:
            upperbound = middle
    return lowerbound
# ==========================================================


# ==========================================================
# def linkList_sort(args): Insertion Sort with linked list
# ==========================================================
class Node:
    key = None
    next = None

    def __init__(self):
        key = None
        next = None


def linked_list(xs):
    n = len(xs)
    head = Node()
    head.key = xs[0]
    node = head
    for i in range(1, n):
        term = Node()
        term.key = xs[i]
        node.next = term
        node = node.next
    return head


def linklist_insert(xn, x):
    head = xn
    p = None
    finder = xn
    while finder is not None and x.key > finder.key:
        p = finder
        finder = finder.next

    x.next = finder
    if p is None:
        return x

    p.next = x
    return head


def linklist_sort(xs):
    head = Node()
    head.key = xs[0]
    for i in range(1, len(xs)):
        node = Node()
        node.key = i
        head = linklist_insert(head, node)

    return head
# ==========================================================

# ==========================================================

# ==========================================================
class TreeNode:
    key = None
    left = None
    right = None
    parent = None

    def __init__(self):
        key = None
        left = None
        right = None
        parent = None


def bst_insert(tree, k):
    root = tree
    parent = None
    x = TreeNode()
    x.key = k
    while tree is not None:
        parent = tree
        if x.key > tree.key:
            tree = tree.right
        else:
            tree = tree.left

    x.parent = parent
    if parent is None:
        return x
    if parent.key > x.key:
        parent.left = x
    else:
        parent.right = x

    return root


def in_order(tree):
    if tree:
        if tree.left:
            in_order(tree.left)
        print tree.key
        if tree.right:
            in_order(tree.right)


def bst(xs):
    root = TreeNode()
    root.key = xs[0]
    for i in range(1, len(xs)):
        root = bst_insert(root, i)

    return root