# Recursive Solution    [N -> Number of tree nodes]
# O(N) TC   [Visit all the nodes of the tree once]
# O(N) SC   [Worst case scenario -> Skewed Tree]

def inorderTraversal(root):
    traversalResult = []
    # edge case
    if root == None:
        return traversalResult
    
    # functin to populate result of traversal
    traverseInorder(root, traversalResult)
    return traversalResult


# Helper Method
def traverseInorder(root, traversalResult):
    # base case
    if root == None:
        return
    # logic
    traverseInorder(root.left, traversalResult)
    traversalResult.append(root.val)
    traverseInorder(root.right, traversalResult)



# Leetcode: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# GFG: https://practice.geeksforgeeks.org/problems/inorder-traversal/1