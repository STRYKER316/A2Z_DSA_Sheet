# O(N) TC | O(N) SC     [N -> Number of tree nodes]

from collections import deque

def zigzagLevelOrder(root):
    # edge case
    if root == None:    return []

    zigzagTraversalResult = []
    nodeDeque = deque()
    nodeDeque.append(root)
    isReverseDirection = False

    while len(nodeDeque) > 0:
        # process the nodes of the current level in the required direction
        currentLevelTraversal = []
        currentDequeLength = len(nodeDeque)

        if not isReverseDirection:
            for _ in range(currentDequeLength):
                currentNode = nodeDeque.popleft()
                currentLevelTraversal.append(currentNode.val)
                # push its children into queue in (left, right) order
                if currentNode.left != None:
                    nodeDeque.append(currentNode.left)
                if currentNode.right != None:
                    nodeDeque.append(currentNode.right)
        elif isReverseDirection:
            for _ in range(currentDequeLength):
                currentNode = nodeDeque.pop()
                currentLevelTraversal.append(currentNode.val)
                # push its children into queue in (right, left) order
                if currentNode.right != None:
                    nodeDeque.appendleft(currentNode.right)
                if currentNode.left != None:
                    nodeDeque.appendleft(currentNode.left)
        
        # record the current level and update direction
        zigzagTraversalResult.append(currentLevelTraversal)
        isReverseDirection = not isReverseDirection

        return zigzagTraversalResult



# Leetcode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# GFG: https://practice.geeksforgeeks.org/problems/zigzag-tree-traversal/1
# CN: https://www.codingninjas.com/studio/problems/1062662