__author__ = 'Liruo_000'
import Tree


# Exercise 1.1 Problem 1 & 2
list_pre_order = [1, 2, 4, 3, 5, 6]
list_in_order  = [4, 2, 1, 5, 3, 6]


def build_tree(pre_order, in_order):
    index = []
    root = Tree.Node(pre_order[0])
    for x in range(1, len(pre_order)):
        index.append(in_order.index(x))

        stack.append(x)
        index = in_order.index(x)

    '''
            Let's take a break
    '''





'''
this_node = Tree.Node(3)
Tree.insert(this_node, 4)
Tree.insert(this_node, 2)
Tree.insert(this_node, 1)
Tree.insert(this_node, 6)
Tree.insert(this_node, 5)
#pre_order(this_node)
Tree.in_order(this_node)
node_four = Tree.Node(4)
Tree.delete2(this_node, Tree.search(this_node,1))
Tree.in_order(this_node)
#post_order(this_node)
'''