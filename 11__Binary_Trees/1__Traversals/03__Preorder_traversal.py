# Recursive Solution    [N -> Number of tree nodes]
# O(N) TC   [Visit all the nodes of the tree once]
# O(H) SC   [Recursion Call Stack]

def preorderTraversal( root):
    traversalResult = []
    # function to populate the preorder traversal result
    preorderTraversal(root, traversalResult)
    return traversalResult


# Helper Method
def preorderTraversal(root, traversalResult):
    # base case
    if root == None:
        return
    
    # logic
    traversalResult.append(root.val)
    preorderTraversal(root.left, traversalResult)
    preorderTraversal(root.right, traversalResult)



# GFG: https://practice.geeksforgeeks.org/problems/preorder-traversal/1
# CN: https://www.codingninjas.com/studio/problems/preorder-traversal_3838888