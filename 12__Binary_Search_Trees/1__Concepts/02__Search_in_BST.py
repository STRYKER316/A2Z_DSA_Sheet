# O(logN) TC | O(1) SC      [N -> NUmber of Tree nodes]

def searchBST(root, val):
    while root != None:
        # check for current node
        if root.val == val:
            return True
        # move to one of the subtrees
        if root.val > val:
            root = root.left
        else:   root = root.right
    
    return False



# Leetcode: https://leetcode.com/problems/search-in-a-binary-search-tree/
# CN: https://www.codingninjas.com/studio/problems/search-in-bst_1402878