# O(N) TC | O(H) TC     [N -> Number of tree nodes | H -> Recursion call stack Length]

def maxPathSum(root):
    # reference variable to be passed around during recursive calls
    maxPathSum = [float('-inf')]
    # following function will return max-sum path through root 
    # and simultaneously calculate max-sum path through root using root as the pivot point
    rootThroughPathSum = getMaxPathSum(root, maxPathSum)
    
    return max(rootThroughPathSum, maxPathSum[0])


# Helper Method
def getMaxPathSum(root, maxPathSum):
    ## Base case
    if root == None:    return 0
    
    ## Logic
    leftSubtreeMaxPathSum = max(0, getMaxPathSum(root.left, maxPathSum))
    rightSubtreeMaxPathSum = max(0, getMaxPathSum(root.right, maxPathSum))
    # update refrence variable for maxPathSum if needed
    currentRootPathSum = root.val + leftSubtreeMaxPathSum + rightSubtreeMaxPathSum
    maxPathSum[0] = max(currentRootPathSum, maxPathSum[0])
    
    return root.val + max(leftSubtreeMaxPathSum, rightSubtreeMaxPathSum)



# GFG: https://practice.geeksforgeeks.org/problems/maximum-path-sum-from-any-node/1
# Leetcode: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# CN: https://www.codingninjas.com/studio/problems/binary-tree-maximum-path-sum_1280142