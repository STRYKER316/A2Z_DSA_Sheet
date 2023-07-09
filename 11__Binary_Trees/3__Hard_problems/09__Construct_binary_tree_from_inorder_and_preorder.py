class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(N) TC | O(N) SC     [N -> Number of tree nodes]
def buildTree(preorder, inorder):
    arrayLen = len(preorder)
    # make {value : idx} map from inorder traversal
    inorderValueIdxMap = {}
    for i in range(arrayLen):
        inorderValueIdxMap[inorder[i]] = i
    
    rootNode = makeBinaryTree(inorder, 0, arrayLen - 1, preorder, 0, arrayLen - 1, inorderValueIdxMap)
    return rootNode


# Helper method
def makeBinaryTree(inorder, inStart, inEnd, preorder, preStart, preEnd, inorderValueIdxMap):
    # Base case
    if inStart > inEnd or preStart > preEnd:
        return None
    
    # find the root node
    root = preorder[preStart]
    rootIdx = inorderValueIdxMap[root]
    rootNode = TreeNode(root)
    # count nodes in left subtree
    leftNodesCount = rootIdx - inStart
    
    # create left and right subtrees
    leftSubtree = makeBinaryTree(inorder, inStart, rootIdx - 1, preorder, preStart + 1, preStart + leftNodesCount, inorderValueIdxMap)
    rootNode.left = leftSubtree
    rightSubtree = makeBinaryTree(inorder, rootIdx + 1, inEnd, preorder, preStart + leftNodesCount + 1, preEnd, inorderValueIdxMap)
    rootNode.right = rightSubtree
    return rootNode



# Leetcode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# CN: https://www.codingninjas.com/studio/problems/construct-binary-tree-from-inorder-and-preorder-traversal_920539