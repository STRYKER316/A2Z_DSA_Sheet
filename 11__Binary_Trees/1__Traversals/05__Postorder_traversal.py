# Recursive Solution    [N -> Number of tree nodes]
# O(N) TC   [Visit all the nodes of the tree once]
# O(N) SC   [Worst case scenario -> Skewed Tree]

def postorderTraversal(root):
    traversalResult = []
    # edge case
    if root == None:
        return traversalResult
    
    # functin to populate result of traversal
    traversePostorder(root, traversalResult)
    return traversalResult


# Helper Method
def traversePostorder(root, traversalResult):
    # base case
    if root == None:
        return
    # logic
    traversePostorder(root.left, traversalResult)
    traversePostorder(root.right, traversalResult)
    traversalResult.append(root.val)



# Letcode: https://leetcode.com/problems/binary-tree-postorder-traversal/
# GFG: https://practice.geeksforgeeks.org/problems/postorder-traversal/1