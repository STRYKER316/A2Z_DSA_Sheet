# O(1) TC | O(1) SC

def createTree(nodes):
    # create root node and its children
    root = Node(nodes[0])
    root.left = Node(nodes[1])
    root.right = Node(nodes[2])
    # create children nodes for children nodes of root
    root.left.left = Node(nodes[3])
    root.left.right = Node(nodes[4])
    root.right.left = Node(nodes[5])
    root.right.right = Node(nodes[6])

    return root


# --------------------------------------
class Node:
    def __init__(self, val):
        self.date = val
        self.left = None
        self.right = None
# --------------------------------------



# CN: https://www.codingninjas.com/studio/problems/create-binary-tree_8360671
# GFG: https://practice.geeksforgeeks.org/problems/binary-tree-representation/1s