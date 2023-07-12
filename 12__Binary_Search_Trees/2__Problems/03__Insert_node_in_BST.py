class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(H) TC | O(1) SC      [H -> Height of BST]
def insertIntoBST(root, val):
    # edge case
    if root == None:    return TreeNode(val)

    prevNode = None
    currNode = root
    while currNode != None:
        if val > currNode.val:
            prevNode = currNode
            currNode = currNode.right
        else:
            prevNode = currNode
            currNode = currNode.left
    # insert the new node as a child node
    newNode = TreeNode(val)
    if val > prevNode.val:
        prevNode.right = newNode
    else:   prevNode.left = newNode

    return root



# Leetcode: https://leetcode.com/problems/insert-into-a-binary-search-tree/
# CN: https://www.codingninjas.com/studio/problems/insert-into-a-binary-search-tree_1279913