# O(N) TC | O(H) SC     [N -> Numbr of tree nodes | H -> Height of tree]

def isSymmetric(root):
    # edge case
    if root == None:
        return True
    # if the subtrees are mirror images of each othr, then the main tree is symmetric
    return areMirrorImageTrees(root.left, root.right)


# Helper Method
def areMirrorImageTrees(root1, root2):
    # base case
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False

    # logic
    return root1.data == root2.data and areMirrorImageTrees(root1.left, root2.right) and areMirrorImageTrees(root1.right, root2.left)



# Leetcode: https://leetcode.com/problems/symmetric-tree/
# GFG: https://practice.geeksforgeeks.org/problems/symmetric-tree/1
# CN: https://www.codingninjas.com/studio/problems/symmetric-tree_981177