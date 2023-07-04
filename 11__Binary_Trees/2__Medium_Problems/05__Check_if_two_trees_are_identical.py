# --------------- Recursive Solution ---------------
# O(min(N1, N2)) TC | O(min(H1, H2)) SC     [Nx -> Number of Nodes of tree x | Hx -> Height of tree x]

def isIdentical(root1, root2):
    return areIdentical(root1, root2)

# Helper Recursive Method
def areIdentical(root1, root2):
    # base cases
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    # logic
    return root1.data == root2.data and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)



# GFG: https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1
# Leetcode: https://leetcode.com/problems/same-tree/
# CN: https://www.codingninjas.com/studio/problems/799364