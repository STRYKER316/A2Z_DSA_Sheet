# ------------------- Solution 1 -------------------
# O(N) TC | O(H) SC

def lowestCommonAncestor(root, node1, node2):
    # get the root to node path for node p
    pathArrayForNode1 = []
    searchNode(root, node1, pathArrayForNode1)
    pathArrayForNode1.reverse()
    # get the root to node path for node p
    pathArrayForNode2 = []
    searchNode(root, node2, pathArrayForNode2)
    pathArrayForNode2.reverse()

    # find the first common node in both the paths
    lcaNode = pathArrayForNode1[0]
    for i in range(1, min(len(pathArrayForNode1), len(pathArrayForNode2))):
        if pathArrayForNode1[i] != pathArrayForNode2[i]:
            break
        else:   lcaNode = pathArrayForNode1[i]
    
    return lcaNode


# Helper method
def searchNode(root, nodeToFind, pathArray):
    # Base case
    if root == None:    return False

    # Logic
    if root == nodeToFind or searchNode(root.left, nodeToFind, pathArray) or searchNode(root.right, nodeToFind, pathArray):
        pathArray.append(root)
        return True
    return False


# ------------------- Solution 2 -------------------
# O(N) TC | O(H) SC

def lowestCommonAncestor(root, node1, node2):
    lcaNode = findLcaHelper(root, node1, node2)
    return lcaNode


# Helper Method
def findLcaHelper(root, node1, node2):
    # Base case
    if root == None or root == node1 or root == node2:
        return root

    leftSubtreeLcaNode = findLcaHelper(root.left, node1, node2)
    rightSubtreeLcaNode = findLcaHelper(root.right, node1, node2)
    # check if we found the LCA node in one of the subtrees
    if leftSubtreeLcaNode == None:
        return rightSubtreeLcaNode
    if rightSubtreeLcaNode == None:
        return leftSubtreeLcaNode
    # if we got result from both subtrees, then root is the LCA node
    return root



# Leetcode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# GFG: https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-binary-tree/1
# CN: https://www.codingninjas.com/studio/problems/lca-in-a-bst_981280