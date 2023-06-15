# ----------- Itearative Solution -----------
# O(log(n)) TC | O(1) SC

def binarysearch(arr, n, k):
    leftIdx, rightIdx = 0, n - 1
    midIdx = 0

    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # check for the element
        if arr[midIdx] == k:
            return midIdx
        elif arr[midIdx] < k:
            leftIdx = midIdx + 1
        elif arr[midIdx] > k:
            rightIdx = midIdx - 1

    return -1


# ---------- Recursive Solution -------
# O(log(n)) TC | O(log(n)) SC

def binarySearch(arr, n, k):
    leftIdx, rightIdx = 0, n - 1
    return binarySearchHelper(arr, k, leftIdx, rightIdx)


# Helper Method
def binarySearchHelper(array, target, leftIdx, rightIdx):
    # Base case
    if leftIdx > rightIdx:
        return -1    
    
    midIdx = (leftIdx + rightIdx) // 2
    if array[midIdx] == target:
        return midIdx
    elif array[midIdx] < target:
        return binarySearchHelper(array, target, midIdx + 1, rightIdx)
    elif array[midIdx] > target:
        return binarySearchHelper(array, target, leftIdx, midIdx - 1)



# GFG: https://practice.geeksforgeeks.org/problems/binary-search-1587115620/1
# Leetcode: https://leetcode.com/problems/binary-search/
# CN: https://www.codingninjas.com/codestudio/problems/binary-search_972