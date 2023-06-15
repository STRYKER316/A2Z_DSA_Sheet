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



# GFG: https://practice.geeksforgeeks.org/problems/second-largest3735/1
# CN: https://www.codingninjas.com/codestudio/problems/ninja-and-the-second-order-elements_6581960