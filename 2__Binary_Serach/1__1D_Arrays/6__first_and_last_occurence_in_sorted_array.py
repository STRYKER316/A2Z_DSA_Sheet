# O(log(arrayLen)) TC | O(1) SC

def searchRange(nums, target):
    arrayLen = len(nums)
    firstOccurenceIdx = getFirstOccurenceIdx(nums, arrayLen, target)
    lastOccurenceIdx = getLastOccurenceIdx(nums, arrayLen, target)

    return [firstOccurenceIdx, lastOccurenceIdx]


# Helper Method1
def getFirstOccurenceIdx(array, arrayLen, target):
    firstOccurenceIdx = float('inf')
    
    leftIdx, rightIdx = 0, arrayLen - 1
    midIdx = 0
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # search for target
        if array[midIdx] == target:
            # update the naswer if needed
            if midIdx < firstOccurenceIdx:
                firstOccurenceIdx = midIdx
            rightIdx = midIdx - 1
        elif array[midIdx] > target:
            rightIdx = midIdx - 1
        else:
            leftIdx = midIdx + 1
    
    if firstOccurenceIdx == float('inf'):
        return -1
    return firstOccurenceIdx


# Helper Method2
def getLastOccurenceIdx(array, arrayLen, target):
    lastOccurenceIdx = float('-inf')
    
    leftIdx, rightIdx = 0, arrayLen - 1
    midIdx = 0
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # search for target
        if array[midIdx] == target:
            # update the naswer if needed
            if midIdx > lastOccurenceIdx:
                lastOccurenceIdx = midIdx
            leftIdx = midIdx + 1
        elif array[midIdx] > target:
            rightIdx = midIdx - 1
        else:
            leftIdx = midIdx + 1
    
    if lastOccurenceIdx == float('-inf'):
        return -1
    return lastOccurenceIdx


# GFG: https://bit.ly/3QuCFEP
# Leetcode: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# CN: https://www.codingninjas.com/codestudio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549