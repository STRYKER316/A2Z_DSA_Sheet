# ------ Reverse array Logic ------
# O(N) TC | O(1) SC

def leftRotate(arr, n, d):
    # update d
    d = d % n
    if d == 0:  return arr
    
    # reverse the array
    reverseArray(arr, 0, n - 1)
    # reverse the array in parts
    reverseArray(arr, 0, n - d - 1)
    reverseArray(arr, n - d, n - 1)
    
    return arr


# Helper Method
def reverseArray(arr, start, end):
    left, right = start, end
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# GFG: https://practice.geeksforgeeks.org/problems/reversal-algorithm5340/1
# Leetcode: https://leetcode.com/problems/rotate-array/
# CN: https://www.codingninjas.com/codestudio/problems/rotate-array_1230543