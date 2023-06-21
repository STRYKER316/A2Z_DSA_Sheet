# O(N) TC | O(1) SC     [N -> length of LinkedList]

def getCount(headNode):
    # empty list check
    if headNode == None:   return 0
    
    nodeCount = 0
    currentNode = headNode
    while currentNode != None:
        nodeCount += 1
        currentNode = currentNode.next
    
    return nodeCount


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None



# GFG: https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/0