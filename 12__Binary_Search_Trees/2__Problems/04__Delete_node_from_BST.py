# O(H) TC | O(H) SC     [H -> Height of BST]

# Recursive Solution
# Assumption: Function deletes the node with the key as value and returns the root of the updated tree
def deleteNode(root, key):
    # Base case
    if root == None:    return root
    
    # Logic
    if key < root.data:
        root.left = deleteNode(root.left, key)
    elif key > root.data:
        root.right = deleteNode(root.right, key)
    else:
        if root.left == None and root.right == None:    # root is a leaf node
            return None
        elif root.left == None:     # root only has a right subtree
            return root.right
        elif root.right == None:    # root only has a left subtree
            return root.left
        else:                       # root has a left and a right subtree
            lstMax = getMaxInBST(root.left)
            root.data = lstMax
            root.left = deleteNode(root.left, lstMax)
    
    return root


# Helper Method
def getMaxInBST(root):
    while root.right != None:
        root = root.right
    return root.data



# Leetcode: https://leetcode.com/problems/delete-node-in-a-bst/
# CN: https://www.codingninjas.com/studio/problems/delete-node-in-bst_920381a