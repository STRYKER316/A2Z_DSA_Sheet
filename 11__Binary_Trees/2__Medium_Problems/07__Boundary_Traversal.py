# O(N) TC | O(N) SC     [N -> Number of tree nodes]

def traverseBoundary(root):
    # edge case
    if root == None:    return []
        
    boundaryTraversalResult = []
    if not isLeafNode(root):
        boundaryTraversalResult.append(root.data)
    # get left boundary, leaf nodes and right boundary traversals
    leftBoundaryTraversal = getLeftBoundaryTraversal(root.left)
    leafNodesTraversal = getLeafNodesTraversal(root)
    rightBoundaryTraversal = getRightBoundaryTraversal(root.right)
    rightBoundaryTraversal.reverse()
    # accumulate the answers
    boundaryTraversalResult.extend(leftBoundaryTraversal)
    boundaryTraversalResult.extend(leafNodesTraversal)
    boundaryTraversalResult.extend(rightBoundaryTraversal)

    return boundaryTraversalResult


# Helper Method 1
def isLeafNode(node):
    return node.left == None and node.right == None


# Helper Method 2
def getLeftBoundaryTraversal(currentNode):
    traversalResult = []
    while currentNode != None:
        if isLeafNode(currentNode):
            break
        traversalResult.append(currentNode.data)
        # got to its left child, if not then right child
        if currentNode.left != None:
            currentNode = currentNode.left
        else:   currentNode = currentNode.right
    
    return traversalResult


# Helper Method 3
def getRightBoundaryTraversal(currentNode):
    traversalResult = []
    while currentNode != None:
        if isLeafNode(currentNode):
            break
        traversalResult.append(currentNode.data)
        # got to its left child, if not then right child
        if currentNode.right != None:
            currentNode = currentNode.right
        else:   currentNode = currentNode.left
    
    return traversalResult


# Helper Method 4
def getLeafNodesTraversal(root):
    traversalResult = []
    getLeafNodesTraversalHelper(root, traversalResult)
    return traversalResult

# Helper Method 4.1
def getLeafNodesTraversalHelper(root, traversalResult):
    # base case
    if root == None:    return
    # logic
    if isLeafNode(root):
        traversalResult.append(root.data)
        return
    getLeafNodesTraversalHelper(root.left, traversalResult)
    getLeafNodesTraversalHelper(root.right, traversalResult)



# GFG: https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/0
# CN: https://www.codingninjas.com/studio/problems/boundary-traversal_790725