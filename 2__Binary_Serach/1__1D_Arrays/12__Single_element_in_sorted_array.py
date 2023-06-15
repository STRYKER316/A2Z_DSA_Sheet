# O(log(arrayLen)) | O(1) SC

def singleNonDuplicate(nums):
    arrayLen = len(nums)
    # edge case
    if arrayLen == 1:  return nums[0]
    # check if strat and end elements are unique
    if nums[0] != nums[1]:    return nums[0]
    if nums[-1] != nums[-2]:  return nums[-1]
    
    singleElement = None
    leftIdx, rightIdx = 1, arrayLen - 2
    midIdx = 0
    
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # current number check
        if nums[midIdx] != nums[midIdx - 1] and nums[midIdx] != nums[midIdx + 1]:
            singleElement = nums[midIdx]
            break
        
        # 1st occurence of pair check
        elif nums[midIdx] == nums[midIdx + 1]:
            if midIdx % 2 == 0:
                leftIdx = midIdx + 1
            else:   rightIdx = midIdx - 1
        
        # 2nd occurence of pair check
        elif nums[midIdx] == nums[midIdx - 1]:
            if midIdx % 2 != 0:
                leftIdx = midIdx + 1
            else:   rightIdx = midIdx - 1
    
    return singleElement



# GFG: https://practice.geeksforgeeks.org/problems/find-the-element-that-appears-once-in-sorted-array0624/1
# Leetcode: https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# CN: https://www.codingninjas.com/codestudio/problems/unique-element-in-sorted-array_1112654