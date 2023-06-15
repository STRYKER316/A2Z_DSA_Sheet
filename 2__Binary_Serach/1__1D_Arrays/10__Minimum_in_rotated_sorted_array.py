# O(log(arrayLen)) TC | O(1) SC

def findMin(nums):
    # no rotation check
    if nums[0] < nums[-1]:    return nums[0]
    
    minValue = float('inf')
    leftIdx, rightIdx = 0, len(nums) - 1
    midIdx = 0
    
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # check if left half is sorted
        if nums[leftIdx] <= nums[midIdx]:
            minValue = min(minValue, nums[leftIdx])
            leftIdx = midIdx + 1
        # else right half is sorted
        else:
            minValue = min(minValue, nums[midIdx])
            rightIdx = midIdx - 1
    
    return minValue



# GFG: https://practice.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1
# Leetcode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# CN: https://www.codingninjas.com/codestudio/problems/rotated-array_1093219