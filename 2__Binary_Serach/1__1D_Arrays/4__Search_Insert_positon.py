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



# Link: https://leetcode.com/problems/search-insert-position/
# Link: https://bit.ly/3pFDbUN
# Link: https://www.codingninjas.com/codestudio/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813