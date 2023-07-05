# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

# --------------- Version1: Complete Traversal ---------------
def levelOrder(root):
    # edge case
    if root == None:    return []
    
    levelOrderTraversalResult = []
    nodeQueue = deque()
    nodeQueue.append(root)

    while len(nodeQueue) > 0:
        # pop the first node and record it
        topNode = nodeQueue.popleft()
        levelOrderTraversalResult.append(topNode.val)

        # push its children into queue, if there are any
        if topNode.left != None:
            nodeQueue.append(topNode.left)
        if topNode.right != None:
            nodeQueue.append(topNode.right)

    return levelOrderTraversalResult


# --------------- Version2: Level by Level Traversal ---------------
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
        # iterate through all the nodes for the current level that are in the queue
        for _ in range(currentQueueLength):
            currentNode = nodeQueue.popleft()
            currentLevelNodes.append(currentNode.val)
            # insert the children into nodeQueue, if there are any
            if currentNode.left != None:
                nodeQueue.append(currentNode.left)
            if currentNode.right != None:
                nodeQueue.append(currentNode.right)
        
        # record the nodes of current level
        levelOrderTraversalResult.append(currentLevelNodes)
    
    return levelOrderTraversalResult



# Leetcode: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# CN: https://www.codingninjas.com/studio/problems/796002