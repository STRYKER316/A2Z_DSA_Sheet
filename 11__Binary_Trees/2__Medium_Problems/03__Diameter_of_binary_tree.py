# O(N) TC | O(H) SC     [N -> Number of tree nodes | H -> Recursion call stack]

def diameterOfBinaryTree(root):
    # reference to be passed around during recursive calls
    maxDiameter = [0]
    # following function will calculate tree height and simultaneously update maxDiameter when we find a bigger diameter
    calculateTreeHeight(root, maxDiameter)
    
    return maxDiameter[0]


# Helper Method
def calculateTreeHeight(root, maxDiameter):
    ## Base case
    if root == None:    return 0
    
    ## Logic
    leftSubtreeHeight = calculateTreeHeight(root.left, maxDiameter)
    rightSubtreeHeight = calculateTreeHeight(root.right, maxDiameter)
    # update the reference variable in-case we find a bigger diameter
    currentDiameter = leftSubtreeHeight + rightSubtreeHeight + 1
    maxDiameter[0] = max(currentDiameter, maxDiameter[0])
    
    return 1 + max(leftSubtreeHeight, rightSubtreeHeight)


# GFG: https://practice.geeksforgeeks.org/problems/diameter-of-binary-tree/1
# Leetcode: https://leetcode.com/problems/diameter-of-binary-tree/
# CN: https://www.codingninjas.com/studio/problems/920552