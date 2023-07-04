# O(N) | O(N) SC    [N -> Number of tree nodes]

from collections import deque

def zigzagLevelOrder(root):
    # edge case
    if root == None:    return []
    
    spiralLevelOrderTraversalResult = []
    nodeQueue = deque()
    nodeQueue.append(root)
    isReverseDirection = True
    
    while len(nodeQueue) > 0:
        currentLevelNodes = []
        currentQueueLength = len(nodeQueue)
        
        for _ in range(currentQueueLength):
            currentNode = nodeQueue.popleft()
            currentLevelNodes.append(currentNode.data)
            # push the children into stack in (left, right) order
            if currentNode.left != None:
                nodeQueue.append(currentNode.left)
            if currentNode.right != None:
                nodeQueue.append(currentNode.right)
        
        # check if we need to reverse the result for current level
        if isReverseDirection:
            currentLevelNodes.reverse()
        spiralLevelOrderTraversalResult.extend(currentLevelNodes)
        # update direction
        isReverseDirection = not isReverseDirection
    
    return spiralLevelOrderTraversalResult



# GFG: https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1