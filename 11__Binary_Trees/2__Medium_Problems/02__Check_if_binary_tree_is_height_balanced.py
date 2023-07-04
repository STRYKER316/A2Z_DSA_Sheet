# ---------------- Naive Approach ----------------
# O(N^2) TC | O(N) SC   [N -> Number of tree nodes]

def isBalanced(root):
    return isHeightBalanced(root)


# Helper Method 1
def isHeightBalanced(root):
    # base case
    if root == None:
        return True
    # logic
    leftSubtreeMaxHeight = getMaxHeight(root.left)
    rightSubtreeMaxHeight = getMaxHeight(root.right)
    return abs(leftSubtreeMaxHeight - rightSubtreeMaxHeight) <= 1 and isHeightBalanced(root.left) and isHeightBalanced(root.right)


# Helper method 2
def getMaxHeight(root):
    # base case
    if root == None:
        return 0
    # logic
    leftSubtreeMaxHeight = getMaxHeight(root.left)
    rightSubtreeMaxHeight = getMaxHeight(root.right)
    return 1 + max(leftSubtreeMaxHeight, rightSubtreeMaxHeight)



# ---------------- Optimal Approach ----------------
# O(N) TC | O(N) SC   [N -> Number of tree nodes]
def isBalanced(root):
    pass



# GFG: https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1
# Leetcode: https://leetcode.com/problems/balanced-binary-tree/
# CN: https://www.codingninjas.com/studio/problems/975497s