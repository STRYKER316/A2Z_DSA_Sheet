# Node Class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------------- Solution 1 ----------------
# O(N) TC | O(H) SC     [N -> Number of Tree nodes | H -> Height of BST]

def bstFromPreorder(preorder):
    upperBound = float('inf')
    idxArray = [0]
    return buildBST(preorder, idxArray, upperBound)

# Helper Method
def buildBST(preOrder, idxArray, upperBound):
    # Base case
    if idxArray[0] >= len(preOrder) or preOrder[idxArray[0]] > upperBound:
        return None
    
    # Create the root node and upate idxArray
    currentIdx = idxArray[0]
    root = TreeNode(preOrder[currentIdx])
    idxArray[0] = currentIdx + 1
    # construct left and right subtree
    root.left = buildBST(preOrder, idxArray, root.val)
    root.right = buildBST(preOrder, idxArray, upperBound)
    return root


# ---------------- Solution 2 ----------------
# O(N*H) TC | O(1) SC     [N -> Number of Tree nodes]

def bstFromPreorder(preorder):
    rootNode = TreeNode(preorder[0])
    for i in range(1, len(preorder)):
        insertNodeInBST(rootNode, preorder[i])
    return rootNode

# Helper Method
def insertNodeInBST(root, val):
    prevNode = None
    currNode = root
    # get to the insertion position
    while currNode != None:
        if val > currNode.val:
            prevNode = currNode
            currNode = currNode.right
        else:
            prevNode = currNode
            currNode = currNode.left
    
    # insert the new node as a child of prevNode
    newNode = TreeNode(val)
    if val > prevNode.val:
        prevNode.right = newNode
    else: prevNode.left = newNode



# Leetcode: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# CN: https://www.codingninjas.com/studio/problems/construct-bst-from-preorder-traversal_2689307