# O(N) | O(N) SC    [N -> Number of tree nodes]

from collections import deque

def zigzagLevelOrder(root):
    # edge case
    if root == None:    return []
    
    spiralLevelOrderTraversalResult = []
    nodeDeque = deque()
    nodeDeque.append(root)
    
    isReverse = False
    while len(nodeDeque) > 0:
        currentQueueLength = len(nodeDeque)
        currentLevelraversal = []
        
        if not isReverse:
            # traverse the level from left to right
            for _ in range(currentQueueLength):
                currentNode = nodeDeque.popleft()
                currentLevelraversal.append(currentNode.val)
                # right append the children into the deque; first leftChild, then rightChild
                if currentNode.left != None:
                    nodeDeque.append(currentNode.left)
                if currentNode.right != None:
                    nodeDeque.append(currentNode.right)
        else:
            # traverse the level from right to left
            for _ in range(currentQueueLength):
                currentNode = nodeDeque.pop()
                currentLevelraversal.append(currentNode.val)
                # left append children into the deque; first rightchild, then leftChild
                if currentNode.right != None:
                    nodeDeque.appendleft(currentNode.right)
                if currentNode.left != None:
                    nodeDeque.appendleft(currentNode.left)
        
        spiralLevelOrderTraversalResult.append(currentLevelraversal)
        # update traverse direction for next level
        isReverse = not isReverse
    
    return spiralLevelOrderTraversalResult



# GFG: https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1