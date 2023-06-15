# O(log(arrayLen)) TC | O(1) SC

def searchInsert(nums, target):
    # Basically same as Lower bound finding algorithm
    ansIdx = len(nums)

    leftIdx, rightIdx = 0, len(nums) - 1
    midIdx = 0
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # condition check
        if nums[midIdx] >= target:
            ansIdx = midIdx
            rightIdx = midIdx - 1
        elif nums[midIdx] < target:
            leftIdx = midIdx + 1
    
    return ansIdx



# GFG: https://practice.geeksforgeeks.org/problems/search-insert-position-of-k-in-a-sorted-array/1
# Leetcode: https://leetcode.com/problems/search-insert-position/
# CN: https://www.codingninjas.com/codestudio/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813