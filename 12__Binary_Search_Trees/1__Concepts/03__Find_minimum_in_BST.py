# O(logN) TC | O(1) SC      [N -> NUmber of Tree nodes]

def minVal(root):
    # edge case
    if root == None:
        return -1
    # keep moving to the left subtree from root till we reach the left-most child
    while root.left != None:
        root = root.left
    return root.data



# CN: https://www.codingninjas.com/studio/problems/minimum-element-in-bst_8160462