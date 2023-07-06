# --------------- Recursive Solurion ---------------
# O(N) TC | O(H) SC     [N -> Number of tree nodes | H -> Height of the tree]

def rightSideView(root):
    rightViewResult = []
    currentLevel = 1
    rightSideViewHelper(root, currentLevel, rightViewResult)
    return rightViewResult

# Helper Method
def rightSideViewHelper(root, currentLevel, rightViewResult):
    # base case
    if root == None:
        return
    # logic
    if currentLevel - len(rightViewResult) == 1:
        rightViewResult.append(root.val)
    rightSideViewHelper(root.right, currentLevel + 1, rightViewResult)
    rightSideViewHelper(root.left, currentLevel + 1, rightViewResult)


# --------------- Iterative Solurion ---------------
# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def rightSideView(root):
    # edge case
    if root == None:    return []
    
    rightView = []
    nodeQueue = deque()
    nodeQueue.append(root)
    
    while len(nodeQueue) > 0:
        lastNode = nodeQueue[-1]
        rightView.append(lastNode.val)
        # pop all the nodes from back of the deque and push their children in right, left order to front of the queue
        for _ in range(len(nodeQueue)):
            currentNode = nodeQueue.pop()
            if currentNode.right != None:
                nodeQueue.appendleft(currentNode.right)
            if currentNode.left != None:
                nodeQueue.appendleft(currentNode.left)
    return rightView



# Leetcode: https://leetcode.com/problems/binary-tree-right-side-view/