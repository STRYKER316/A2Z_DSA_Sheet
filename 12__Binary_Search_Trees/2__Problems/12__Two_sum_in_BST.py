# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque

class Solution:
    def findTarget(self, root, k):
        # instantiate a forward and a backward iterator for the BST
        leftIterator = BstIterator(root, False)
        rightIterator = BstIterator(root, True)

        leftVal = leftIterator.next()
        rightVal = rightIterator.next()
        while leftVal < rightVal:
            if leftVal + rightVal == k:
                return True
            elif leftVal + rightVal < k:
                leftVal = leftIterator.next()
            elif leftVal + rightVal > k:
                rightVal = rightIterator.next()
        # out of the loop implies no such pair was foun
        return False



# Helper Class - BST Iterator
class BstIterator():
    def __init__(self, root, isReverse):
        self.isReverse = isReverse
        # initiate a stack to use for BST treversal
        self.nodeStack = deque()
        self.pushNodes(root)
    

    def next(self):
        topNode = self.nodeStack.pop()
        # push nodes into stack w.r.t. topNode before returning
        if not self.isReverse:
            self.pushNodes(topNode.right)
        else:
            self.pushNodes(topNode.left)
        return topNode.val
        
    
    def hasNext(self):
        return len(self.nodeStack) > 0
    
    
    # Helper Method to push required nodes into stack
    def pushNodes(self, root):
        while root != None:
            self.nodeStack.append(root)
            if not self.isReverse:
                root = root.left
            else:
                root = root.right



# Leetcode: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# CN: https://codingninjas.com/studio/problems/pair-sum-in-bst._920493