# --------------- Recursive Solurion ---------------
# O(N) TC | O(H) SC     [N -> Number of tree nodes | H -> Height of the tree]

def LeftView(root):
    currentLevel = 1
    leftViewResult = []
    # recursive helper function to fill up the left-view result
    leftViewRecursiveHelper(root, currentLevel, leftViewResult)
    return leftViewResult

# Helper Method
def leftViewRecursiveHelper(root, currentLevel, leftViewResult):
    # base case
    if root == None:
        return
    # record the current node if we're visiting the level for the first time
    if currentLevel - len(leftViewResult) == 1:
        leftViewResult.append(root.data)
    # recursively visit left subtree, then right subtree
    leftViewRecursiveHelper(root.left, currentLevel + 1, leftViewResult)
    leftViewRecursiveHelper(root.right, currentLevel + 1, leftViewResult)


# --------------- Iterative Solurion ---------------
# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def LeftView(root):
    # edge case
    if root == None:    return []
    
    leftViewResult = []
    nodeQueue = deque()
    nodeQueue.append(root)
    
    while len(nodeQueue) > 0:
        topNode = nodeQueue[0]
        leftViewResult.append(topNode.data)
        # pop all the nodes from front of queue and push their children in left, right order into back of queue
        for _ in range(len(nodeQueue)):
            currentNode = nodeQueue.popleft()
            if currentNode.left != None:
                nodeQueue.append(currentNode.left)
            if currentNode.right != None:
                nodeQueue.append(currentNode.right)
    return leftViewResult



# GFG: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1
# CN: https://www.codingninjas.com/studio/problems/left-view-of-binary-tree_625707
