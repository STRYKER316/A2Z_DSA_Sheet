# --------------- Recursive Solution ---------------
# O(min(N1, N2)) TC | O(min(H1, H2)) SC     [Nx -> Number of Nodes of tree x | Hx -> Height of tree x]

def isIdentical(root1, root2):
    return areIdentical(root1, root2)

# Helper Recursive Method
def areIdentical(root1, root2):
    # base cases
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    # logic
    return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)



# --------------- Iterative Solution ---------------
# O(min(N1, N2)) TC | O(min(N1, N2)) SC     [Nx -> Number of Nodes of tree x]

from collections import deque

def isIdentical(root1, root2):
    # get level order traversal of both the trees
    levelOrderTraversal1 = getLevelOrderTraversal(root1)
    levelOrderTraversal2 = getLevelOrderTraversal(root2)
    
    # compare the results
    if len(levelOrderTraversal1) != len(levelOrderTraversal2):
        return False
    
    for i in range(len(levelOrderTraversal1)):
        if levelOrderTraversal1[i] != levelOrderTraversal2[i]:
            return False
    return True


# Helper Method
def getLevelOrderTraversal(root):
    # edge case
    if root == None:
        return [-1]
    
    # queue for processing level order
    nodeQueue = deque()
    nodeQueue.append(root)
    # store the traversal result
    traversalResult = []
    traversalResult.append(root.data)
    
    while len(nodeQueue) > 0:
        topNode = nodeQueue.popleft()
        # record and push its left chld into queue, if present
        if topNode.left != None:
            traversalResult.append(topNode.left.data)
            nodeQueue.append(topNode.left)
        else:   traversalResult.append(-1)
        # record and push its right chld into queue, if present
        if topNode.right != None:
            nodeQueue.append(topNode.right)
            traversalResult.append(topNode.right.data)
        else: traversalResult.append(-1)
    
    return traversalResult


# GFG: https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1
# Leetcode: https://leetcode.com/problems/same-tree/
# CN: https://www.codingninjas.com/studio/problems/799364