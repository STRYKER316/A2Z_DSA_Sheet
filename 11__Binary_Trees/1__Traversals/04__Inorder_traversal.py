# Recursive Solution    [N -> Number of tree nodes]
# O(N) TC   [Visit all the nodes of the tree once]
# O(H) SC   [Recursion Call Stack]

def inorderTraversal(root):
    traversalResult = []
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



# GFG: https://practice.geeksforgeeks.org/problems/inorder-traversal/1
# CN: https://www.codingninjas.com/studio/problems/inorder-traversal_3839605