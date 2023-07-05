# O(N) TC | O(H) SC     [N -> Number of Treenodes | H -> Height of Tree]

from collections import deque

def postorderTraversal(root):
    # edge case
    if root == None:    return []

    nodeStack = deque()
    nodeStack.append(root)
    traversalResult = []

    while len(nodeStack) > 0:
        # process the top node
        topNode = nodeStack.pop()
        traversalResult.append(topNode.val)
        # push left and right children into stack, if there are any
        if topNode.left != None:
            nodeStack.append(topNode.left)
        if topNode.right != None:
            nodeStack.append(topNode.right)
    
    # reverse the result to get the postorder traversal
    traversalResult.reverse()
    return traversalResult



# Leetcode: https://leetcode.com/problems/binary-tree-postorder-traversal/