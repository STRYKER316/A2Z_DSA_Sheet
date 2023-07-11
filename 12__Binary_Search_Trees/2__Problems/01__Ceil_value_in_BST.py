# O(logN) TC | O(1) SC      [N - > Number of Tree nodes]

def findCeil(root, x):
    ceilValue = -1

    # keep searching tillwe run out of possible nodes to search
    while root != None:
        if root.data == x:
            return root.data
        # record the root-value, whenever the root-value > x and then search for a smaller answer
        if root.data > x:
            ceilValue = root.data
            root = root.left
        else:   root = root.right

    return ceilValue



# CN: https://www.codingninjas.com/studio/problems/ceil-from-bst_920464