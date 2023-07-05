# Recursive Solution    [N -> Number of tree nodes]
# O(N) TC   [Visit all the nodes of the tree once]
# O(H) SC   [Recursion Call Stack]

def postorderTraversal(root):
    traversalResult = []
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



# GFG: https://practice.geeksforgeeks.org/problems/postorder-traversal/1
# CN: https://www.codingninjas.com/studio/problems/postorder-traversal_3839614