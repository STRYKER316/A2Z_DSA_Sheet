# O(N) TC | O(1) SC

def print2largest(array, n):
    firstLargest = -1
    secondLargest = -1
    
    for num in array:
        if num > firstLargest:
            secondLargest = firstLargest
            firstLargest = num
        elif num > secondLargest and num != firstLargest:
            secondLargest = num
    
    return secondLargest



# Link: https://bit.ly/3pFvBcN