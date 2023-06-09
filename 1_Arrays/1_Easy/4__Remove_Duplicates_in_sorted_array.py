# O(N) TC | O(1) SC

def removeDuplicates(nums):
    distinctNumIdx = 0
    
    for i in range(1, len(nums)):
        if nums[i] != nums[distinctNumIdx]:
            distinctNumIdx += 1
            nums[distinctNumIdx] = nums[i]
    
    return distinctNumIdx + 1



# Link: https://bit.ly/3w7b6ck
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/