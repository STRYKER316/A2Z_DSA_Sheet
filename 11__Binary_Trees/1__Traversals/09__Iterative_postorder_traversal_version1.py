# O(N) TC | O(N) SC     [N -> Number of Treenodes]

from collections import deque

# ---------------- Solution 1 (2 Stacks) ----------------
def postOrder(self,node):
    # edge case
    if node == None:
        return []
    
    pushStack = deque()
    popStack = deque()
    pushStack.append(node)
    
    while len(pushStack) > 0:
        # pop the top elements from pushStack and push into popStack
        topNode = pushStack.pop()
        popStack.append(topNode)
        
        # push its left and right children into pushStack, if they exist
        if topNode.left != None:
            pushStack.append(topNode.left)
        if topNode.right != None:
            pushStack.append(topNode.right)
    
    # once pushStack is empty, popping values from popStack gives the postorder traversal
    traversalResult = []
    while len(popStack) > 0:
        topNode = popStack.pop()
        traversalResult.append(topNode.data)
    
    return traversalResult



# GFG: https://practice.geeksforgeeks.org/problems/postorder-traversal-iterative/1