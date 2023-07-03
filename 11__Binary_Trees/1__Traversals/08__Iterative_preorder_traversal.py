# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def preorderTraversal(root):
    # edge case
    if root == None:
        return []
    
    traversalResult = []
    nodeStack = deque()
    nodeStack.append(root)

    while len(nodeStack) > 0:
        # pop the top node from stack to process it
        currentNode = nodeStack.pop()
        traversalResult.append(currentNode.val)
        # check for children and push them into stack
        if currentNode.right != None:
            nodeStack.append(currentNode.right)
        if currentNode.left != None:
            nodeStack.append(currentNode.left)
    
    return traversalResult



# Leetcode: https://leetcode.com/problems/binary-tree-preorder-traversal/description/