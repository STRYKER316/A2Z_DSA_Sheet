# O(N) TC | O(H) SC     [N -> Number of tree nodes | H -> Height of tree]

def pathToNode(root, value):
    pathArray = []
    # Method to find if node is present in the tree, also populate the pathArray from root to node
    isNodeFound(root, value, pathArray)
    pathArray.reverse()
    return pathArray


# Helper Method
def isNodeFound(root, valueToFind, pathArray):
    # Base case
    if root == None:    return False
    
    # Logic
    if root.val == valueToFind or isNodeFound(root.left, valueToFind, pathArray) or isNodeFound(root.right, valueToFind, pathArray):
        pathArray.append(root.val)
        return True
    return False



# InterviewBit: https://www.interviewbit.com/problems/path-to-given-node/