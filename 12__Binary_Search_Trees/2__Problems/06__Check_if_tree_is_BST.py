# O(N) TC | O(H) SC     [N -> Number of tree noes | H -> Height of BST]

from collections import deque

def isValidBST(root):
    prevVal = float('-inf')
    isBst = True

    nodeStack = deque()
    currNode = root
    # use the stack to traverse the tree in inorder fashion
    while True:
        if currNode != None:
            nodeStack.append(currNode)
            currNode = currNode.left
            continue
        # check if we have any node to process in the stack
        if len(nodeStack) > 0:
            topNode = nodeStack.pop()
            if topNode.val <= prevVal:
                isBst = False
                break
            # upadte prevVal for next node
            prevVal = topNode.val
            currNode = topNode.right
        else:   break

    return isBst



# Leetcode: https://leetcode.com/problems/validate-binary-search-tree/
# CN: https://www.codingninjas.com/studio/problems/check-bst_5975