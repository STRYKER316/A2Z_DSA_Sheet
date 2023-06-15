# O(N) TC | O(1) SC

def removeDuplicates(nums):
    distinctNumIdx = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[distinctNumIdx]:
            distinctNumIdx += 1
            nums[distinctNumIdx] = nums[i]
    
    return distinctNumIdx + 1



# GFG: https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
# Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# CN: https://www.codingninjas.com/codestudio/problems/remove-duplicates-from-sorted-array_1102307