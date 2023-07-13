# O(N) TC | O(H) SC     [N -> Number of teee nodes | H -> Height of BST]

from collections import deque

def kthSmallest(root, k):
    nodeStack = deque()
    visitedNodesCount = 0
    kthSmallestNode = 0
    currentNode = root

    # Iterative inorder traversal
    while True:
        if currentNode != None:
            nodeStack.append(currentNode)
            currentNode = currentNode.left
            continue
        # check if we have any node to process in the stack
        if len(nodeStack) > 0:
            topNode = nodeStack.pop()
            visitedNodesCount += 1
            if visitedNodesCount == k:
                kthSmallestNode = topNode.val
                break
            # upadte currentNode for next iteration
            currentNode = topNode.right
        else: break
    
    return kthSmallestNode



# Leetcode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# CN: https://www.codingninjas.com/studio/problems/kth-smallest-node-in-bst_920441