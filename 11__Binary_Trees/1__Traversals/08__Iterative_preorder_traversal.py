# O(N) TC | O(H) SC     [N -> Number of tree nodes | H -> Height of Tree]

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
        # push right child, left child into stack; as stack is LIFO and we want to process left child first
        if currentNode.right != None:
            nodeStack.append(currentNode.right)
        if currentNode.left != None:
            nodeStack.append(currentNode.left)
    
    return traversalResult



# Leetcode: https://leetcode.com/problems/binary-tree-preorder-traversal/description/