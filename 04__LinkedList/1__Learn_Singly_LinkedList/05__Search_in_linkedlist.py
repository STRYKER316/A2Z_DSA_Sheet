# O(N) TC | O(1) SC     [N -> Length of linkedList]

def searchKey(head, key):
    # empty list check
    if head == None:
        return False
    
    isFound = False
    currentNode = head
    while currentNode != None:
        if currentNode.data == key:
            isFound = True
            break
        # iterate to next node
        currentNode = currentNode.next
    
    return isFound


# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



# GFG: https://practice.geeksforgeeks.org/problems/search-in-linked-list-1664434326/1