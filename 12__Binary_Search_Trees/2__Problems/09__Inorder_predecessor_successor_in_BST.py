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



# CN: https://www.codingninjas.com/studio/problems/predecessor-and-successor-in-bst_893049