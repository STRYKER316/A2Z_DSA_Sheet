# O(log(arrayLen)) TC | O(1) SC

def findPeakElement(nums):
    arrayLen = len(nums)
    # edge case
    if arrayLen == 1:  return 0
    # first and last element check
    if nums[0] >= nums[1]:    return 0
    if nums[-1] >= nums[-2]:  return arrayLen - 1
    
    leftIdx, rightIdx = 1, arrayLen - 2
    midIdx = 0
    peakIdx = -1
    
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # current element check
        if nums[midIdx] > nums[midIdx - 1] and nums[midIdx] > nums[midIdx + 1]:
            peakIdx = midIdx
            break
        elif nums[midIdx] <= nums[midIdx + 1]:
            leftIdx = midIdx + 1
        else:
            rightIdx = midIdx - 1
    
    return peakIdx



# GFG: https://bit.ly/3Apsuf3
# Leetcode: https://leetcode.com/problems/find-peak-element/