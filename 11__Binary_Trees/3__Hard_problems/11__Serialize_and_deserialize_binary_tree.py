class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# O(N) TC | O(N) TC     [N -> Number of Tree nodes]
from collections import deque

def serialize(root):
    """Encodes a tree to a single string.
    :type root: TreeNode
    :rtype: str
    """
    serializedTree = []
    nodeQueue = deque()
    nodeQueue.append(root)

    while len(nodeQueue):
        topNode = nodeQueue.popleft()
        # null check
        if topNode == None:
            serializedTree.append('# ')
            continue
        # store the node and push its children nto queue
        serializedTree.append(str(topNode.val) + ' ')
        nodeQueue.append(topNode.left)
        nodeQueue.append(topNode.right)
    # stringify the serialized tree
    return ''.join(serializedTree)


def deserialize(data):
    """Decodes your encoded data to tree and returns the tree root
    :type data: str
    :rtype: TreeNode
    """
    # edge case
    if data[0] == '#':
        return None

    nodeStrings = data.split()
    nodeStringsCount = len(nodeStrings)
    # push the root node into queue
    rootNode = TreeNode(int(nodeStrings[0]))
    nodeQueue = deque()
    nodeQueue.append(rootNode)

    currentIdx = 1
    while len(nodeQueue) > 0 and currentIdx < nodeStringsCount:
        topNode = nodeQueue.popleft()
        # check for left child
        if nodeStrings[currentIdx] != '#':
            leftChild = TreeNode(int(nodeStrings[currentIdx]))
            topNode.left = leftChild
            nodeQueue.append(leftChild)
        currentIdx += 1
        # check for right child
        if nodeStrings[currentIdx] != '#':
            rightChild = TreeNode(int(nodeStrings[currentIdx]))
            topNode.right = rightChild
            nodeQueue.append(rightChild)
        currentIdx += 1
    
    return rootNode



# Leetcode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# CN: https://www.codingninjas.com/studio/problems/serialize-and-deserialize-binary-tree_920328