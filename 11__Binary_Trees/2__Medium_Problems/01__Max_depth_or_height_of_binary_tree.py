# ------------------- Recursive Solution -------------------
# O(N) TC | O(H) SC (Recursion Stack)     [N -> Number of tree nodes | H -> Height of Tree]

def maxDepth(root):
    return getMaxDepth(root)


# Helper Recursive Method
def getMaxDepth(root):
    # base case
    if root == None:
        return 0
    # logic
    leftSubtreeMaxDepth = getMaxDepth(root.left)
    rightSubtreeMaxDepth = getMaxDepth(root.right)
    return 1 + max(leftSubtreeMaxDepth, rightSubtreeMaxDepth)


# ------------------- Iterative Solution -------------------
# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def maxDepth(root):
    # edge case
    if root == None:    return 0

    nodeQueue = deque()
    nodeQueue.append(root)
    currentLevel = 0

    while len(nodeQueue) > 0:
        # process the current level of nodes
        for _ in range(len(nodeQueue)):
            topNode = nodeQueue.popleft()
            # push its child nodes into queue
            if topNode.left != None:
                nodeQueue.append(topNode.left)
            if topNode.right != None:
                nodeQueue.append(topNode.right)
        # update level for the current processed level
        currentLevel += 1
    
    return currentLevel



# GFG: https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
# Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/