# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def verticalOrder(root):
    # track the min and max vertical levels
    maxLevel = float('-inf')
    minLevel = float('inf')
    # queue to store a tuple of (node, vertical level)
    nodeLevelQueue = deque()
    nodeLevelQueue.append((root, 0))
    # record the nodes in level-wise fashion
    nodeLevelMap = {}
    
    # process nodes in level order fashion and store the result in vertical order fashion
    while len(nodeLevelQueue) > 0:
        currentNodeTuple = nodeLevelQueue.popleft()
        currentNode = currentNodeTuple[0]
        currentLevel = currentNodeTuple[1]
        # update level if needed
        maxLevel = max(maxLevel, currentLevel)
        minLevel = min(minLevel, currentLevel)
        
        # record the node for its vertical level and push its children into queue
        if currentLevel not in nodeLevelMap:
            nodeLevelMap[currentLevel] = []
        nodeLevelMap[currentLevel].append(currentNode.data)
        if currentNode.left != None:
            nodeLevelQueue.append((currentNode.left, currentLevel - 1))
        if currentNode.right != None:
            nodeLevelQueue.append((currentNode.right, currentLevel + 1))
    
    # get the traversal result from map
    verticalTraversalResult = []
    for level in range(minLevel, maxLevel + 1):
        verticalTraversalResult.extend(nodeLevelMap[level])
    
    return verticalTraversalResult



# GFG: https://practice.geeksforgeeks.org/problems/print-a-binary-tree-in-vertical-order/1
# CN: https://www.codingninjas.com/studio/problems/vertical-order-traversal_920533
