# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class BSTIterator:
    # Constructor
    def __init__(self, root):
        # initiate a stack for inorder traversal of BST
        self.nodeStack = deque()
        self.pushLeftNodesIntoStack(root)


    # Iterator Method 1
    def next(self) -> int:
        topNode = self.nodeStack.pop()
        # push right subtree of topNode onto the stack before returning
        currentNode = topNode.right
        self.pushLeftNodesIntoStack(currentNode)
        return topNode.val


    # Iterator Method 2
    def hasNext(self) -> bool:
        return len(self.nodeStack) > 0


    # Helper Method
    def pushLeftNodesIntoStack(self, root):
        while root != None:
            self.nodeStack.append(root)
            root = root.left
        return



# Leetcode: https://leetcode.com/problems/binary-search-tree-iterator/