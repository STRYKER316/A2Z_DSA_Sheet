class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(N) TC | O(N) SC     [N -> Number of tree nodes]
def buildTree(inorder, postorder):
    arrayLen = len(inorder)
    # make {value : idx} map for norder array
    inorderValueIdxMap = {}
    for i in range(arrayLen):
        inorderValueIdxMap[inorder[i]] = i
    
    rootNode = makeBinaryTree(inorder, 0, arrayLen - 1, postorder, 0, arrayLen - 1, inorderValueIdxMap)
    return rootNode


# Helper Method
def makeBinaryTree(inorder, inStart, inEnd, postorder, postStart, postEnd, inorderValueIdxMap):
    # Base case
    if inStart > inEnd or postStart > postEnd:
        return None

    # create rootnode
    root = postorder[postEnd]
    rootNode = TreeNode(root)
    rootIdx = inorderValueIdxMap[root]
    # count nodes in left subtree
    leftNodesCount = rootIdx - inStart
    
    # create subtrees
    leftSubtree = makeBinaryTree(inorder, inStart, rootIdx - 1, postorder, postStart, postStart + leftNodesCount - 1, inorderValueIdxMap)
    rootNode.left = leftSubtree
    rightSubtree = makeBinaryTree(inorder, rootIdx + 1, inEnd, postorder, postStart + leftNodesCount, postEnd - 1, inorderValueIdxMap)
    rootNode.right = rightSubtree
    return rootNode



# Leetcode: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# CN: https://www.codingninjas.com/studio/problems/construct-binary-tree-from-inorder-and-postorder-traversal_1266106