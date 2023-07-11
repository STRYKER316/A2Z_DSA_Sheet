def floorInBST(root, X):
    floorVal = -1

    # keep searching tillwe run out of possible nodes to search
    while root != None:
        # check for current root
        if root.data == X:
            return root.data
        # record the root-val whenever the root-val < x and then search for a bigger answer
        if root.data < X:
            floorVal = root.data
            root = root.right
        else:   root = root.left
    
    return floorVal



# GFG: https://practice.geeksforgeeks.org/problems/floor-in-bst/1
# CN: https://www.codingninjas.com/studio/problems/floor-from-bst_920457