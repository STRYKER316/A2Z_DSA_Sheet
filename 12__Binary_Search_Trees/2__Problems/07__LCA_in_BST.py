# O(H) TC | O(1) SC     [H -> Height of BST]

def lowestCommonAncestor(root, node1, node2):
    currentRoot = root
    lcaNode = None

    while True:
        if node1.val < currentRoot.val and node2.val < currentRoot.val:
            currentRoot = currentRoot.left
        elif node1.val > currentRoot.val and node2.val > currentRoot.val:
            currentRoot = currentRoot.right
        else:
            lcaNode = currentRoot
            break
    
    return lcaNode



# Leetcode: httnode1s://leetcode.com/node1roblems/lowest-common-ancestor-of-a-binary-search-tree/