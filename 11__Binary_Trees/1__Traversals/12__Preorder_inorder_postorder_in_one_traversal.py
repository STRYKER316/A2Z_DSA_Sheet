# O(N) TC | O(N) SC     [N -> Number of Tree nodes]

from collections import deque
def getTreeTraversal(root):
    # edge case
    if root == None:    return []

    preOrder = []
    inOrder = []
    postOrder = []

    nodeVisitCountStack = deque()
    nodeVisitCountStack.append((root, 1))

    while len(nodeVisitCountStack) > 0:
        stackTopValue = nodeVisitCountStack.pop()
        currentNode = stackTopValue[0]
        currentVisitCount = stackTopValue[1]

        if currentVisitCount == 1:
            preOrder.append(currentNode.data)
            # mark the node for 2nd visit and push its left children, if present
            nodeVisitCountStack.append((currentNode, 2))
            if currentNode.left != None:
                nodeVisitCountStack.append((currentNode.left, 1))
        
        elif currentVisitCount == 2:
            inOrder.append(currentNode.data)
            # mark the node for 3rd visit and push its right children, if present
            nodeVisitCountStack.append((currentNode, 3))
            if currentNode.right != None:
                nodeVisitCountStack.append((currentNode.right, 1))
        
        elif currentVisitCount == 3:
            postOrder.append(currentNode.data)

    return [inOrder, preOrder, postOrder]



# CN: https://www.codingninjas.com/studio/problems/981269?leftPanelTab=1