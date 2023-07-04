# ------------------- Recursive Solution -------------------
# O(N) TC | O(H) SC     [N -> Number of tree nodes | H -> Height of Tree]

def height(root):
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
def height(root):
    pass



# GFG: https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
# Leetcode: https://leetcode.com/problems/maximum-depth-of-binary-tree/