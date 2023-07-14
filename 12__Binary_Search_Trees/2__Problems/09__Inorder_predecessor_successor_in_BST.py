# --------------- Solution 1 ---------------
# O(H) TC | O(1) SC     [H -> Height of the BST]

def predecessorSuccessor(root, key):
    predecessor, successor = -1, -1

    # iterate till we find the node with given key
    currentRoot = root
    while currentRoot.data != key:
        if currentRoot.data < key:
            predecessor = currentRoot.data
            currentRoot = currentRoot.right
        elif currentRoot.data > key:
            successor = currentRoot.data
            currentRoot = currentRoot.left
    
    # find the max in left-subtree of key-node, if present
    leftSubTree = currentRoot.left
    while leftSubTree != None:
        predecessor = leftSubTree.data
        leftSubTree = leftSubTree.right
    # find the min in right-subtree of key-node, if present
    rightSubTree = currentRoot.right
    while rightSubTree != None:
        successor = rightSubTree.data
        rightSubTree = rightSubTree.left
    
    return [predecessor, successor]


# --------------- Solution 2 ---------------
# O(N) TC | O(N) SC     [N -> Number of tree nodes]

def predecessorSuccessor(root, key):
    # To store the inorder traversal of the BST.
    inorderArray = []
    inorder(root, inorderArray)

    predecessor, successor = -1, -1
    for i in range(len(inorderArray)):
        if inorderArray[i] == key:
            #If predecessor exist.
            if i - 1 >= 0:
                predecessor = inorderArray[i-1]
            # If successor exist.
            if i + 1 < len(inorderArray):
                successor = inorderArray[i+1]
            break
    return [predecessor, successor]


# Helper Method
def inorder(root, inorderArray):
    # Base Case
    if root == None:
        return
    # Logic
    inorder(root.left, inorderArray)
    inorderArray.append(root.data)
    inorder(root.right, inorderArray)



# CN: https://www.codingninjas.com/studio/problems/predecessor-and-successor-in-bst_893049