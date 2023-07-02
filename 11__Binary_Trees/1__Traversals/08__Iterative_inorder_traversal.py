# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def inorderTraversal(root):
    # edge case
    if root == None:
        return []
    
    traversalResult = []
    nodeStack = deque()
    currentNode = root

    while True:
        # keep going left from current node
        if currentNode != None:
            nodeStack.append(currentNode)
            currentNode = currentNode.left
            continue
        
        # if we reached a NULL, process the top node of the stack if present and then move onto its right child
        if len(nodeStack) > 0:
            topNode = nodeStack.pop()
            traversalResult.append(topNode.val)
            currentNode = topNode.right
        else: break

    return traversalResult



# Leetocde: https://leetcode.com/problems/binary-tree-inorder-traversal/