# O(N) TC | O(1) SC     [N -> Length of array]

def constructLL(arr):
    arrayLen = len(arr)
    if arrayLen == 0:
        return None
    
    headNode = Node(arr[0])
    currentNode = headNode
    for i in range(1, arrayLen):
        nextNode = Node(arr[i])
        currentNode.next = nextNode
        currentNode = nextNode
    
    return headNode


# Node definition
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None



# GFG: https://practice.geeksforgeeks.org/problems/introduction-to-linked-list/1