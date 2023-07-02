# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def levelOrder(root):
    # edge case
    if root == None:    return []

    levelOrderTraversalResult = []
    # push the root node into a queue
    nodeQueue = deque()
    nodeQueue.append(root)
    
    # keep iterating till the nodeQueue becomes empty
    while len(nodeQueue) > 0:
        currentLevelNodes = []
        currentQueueLength = len(nodeQueue)
        # iterate through all the nodes in the queue currently and record them
        for _ in range(currentQueueLength):
            currentNode = nodeQueue.popleft()
            currentLevelNodes.append(currentNode.val)
            # insert the children into nodeQueue, if there are any
            if currentNode.left != None:
                nodeQueue.append(currentNode.left)
            if currentNode.right != None:
                nodeQueue.append(currentNode.right)
        
        # record the current lvel of nodes
        levelOrderTraversalResult.append(currentLevelNodes)
    
    return levelOrderTraversalResult



# Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# CN: https://www.codingninjas.com/studio/problems/796002