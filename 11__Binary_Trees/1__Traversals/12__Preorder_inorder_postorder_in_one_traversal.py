# O(N) TC | O(H) SC     [N -> Number of Tree nodes | H -> Height of Tree]

from collections import deque
def getTreeTraversal(root):
    # edge case
    if root == None:    return []

    preOrderTraversal = []
    inOrderTraversal = []
    postOrderTraversal = []

    nodeVisitCountStack = deque()
    nodeVisitCountStack.append((root, 1))

    while len(nodeVisitCountStack) > 0:
        stackTopValue = nodeVisitCountStack.pop()
        currentNode = stackTopValue[0]
        currentVisitCount = stackTopValue[1]

        # 1st time visit to the node
        if currentVisitCount == 1:
            preOrderTraversal.append(currentNode.data)
            # store the node for 2nd visit and push its left children, if present
            nodeVisitCountStack.append((currentNode, 2))
            if currentNode.left != None:
                nodeVisitCountStack.append((currentNode.left, 1))
        # 2nd time visit to the node
        elif currentVisitCount == 2:
            inOrderTraversal.append(currentNode.data)
            # store the node for 3rd visit and push its right children, if present
            nodeVisitCountStack.append((currentNode, 3))
            if currentNode.right != None:
                nodeVisitCountStack.append((currentNode.right, 1))
        # 3rd time visit to node
        elif currentVisitCount == 3:
            postOrderTraversal.append(currentNode.data)

    return [inOrderTraversal, preOrderTraversal, postOrderTraversal]



# CN: https://www.codingninjas.com/studio/problems/981269?leftPanelTab=1