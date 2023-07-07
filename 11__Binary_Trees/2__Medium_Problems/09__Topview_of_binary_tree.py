# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def getTopView(root):
    # edge case
    if root == None:    return []

    # store nodes as (node, verticalLevel) tuples in queue
    nodeQueue = deque()
    nodeQueue.append((root, 0))
    # record nodes of same vertical level in a map as {level : firstNode}
    verticalLevelNodesMap = {}
    minLevel, maxLevel = float('inf'), float('-inf')
    
    while len(nodeQueue) > 0:
        topPair = nodeQueue.popleft()
        currentNode, currentLevel = topPair[0], topPair[1]
        # update the level trackers if needed
        minLevel = min(currentLevel, minLevel)
        maxLevel = max(currentLevel, maxLevel)
        # record the node for its level, if its the first node
        if currentLevel not in verticalLevelNodesMap:
            verticalLevelNodesMap[currentLevel] = currentNode.val
        # push its children into queue
        if currentNode.left != None:
            nodeQueue.append((currentNode.left, currentLevel - 1))
        if currentNode.right != None:
            nodeQueue.append((currentNode.right, currentLevel + 1))
    
    # generate topview from vertical nodes list
    topView = []
    for i in range(minLevel, maxLevel + 1):
        topView.append(verticalLevelNodesMap[i])
    return topView



# GFG: https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1
# CN: https://www.codingninjas.com/studio/problems/799401