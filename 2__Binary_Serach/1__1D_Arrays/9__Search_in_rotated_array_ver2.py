# O(log(N)) TC | O(1) SC -> Average Case
# O(N/2) TC | O(1) SC -> Worst Case
# N -> Length of array

def search(nums, target):
    leftIdx, rightIdx = 0, len(nums) - 1
    midIdx = 0

    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        
        # check if we found target
        if nums[midIdx] == target:
            return True
        # check for all equality case
        if nums[leftIdx] == nums[midIdx] and nums[midIdx] == nums[rightIdx]:
            leftIdx += 1
            rightIdx -= 1
        # check if left half sorted
        elif nums[leftIdx] <= nums[midIdx]:
            if nums[leftIdx] <= target and target <= nums[midIdx]:
                rightIdx = midIdx - 1
            else:   leftIdx = midIdx + 1
        # else right half sorted
        else:
            if nums[midIdx] <= target and target <= nums[rightIdx]:
                leftIdx = midIdx + 1
            else:   rightIdx = midIdx - 1
    
    return False



# GFG: https://bit.ly/3Rm85Nb
# CN: https://www.codingninjas.com/codestudio/problems/search-in-a-rotated-sorted-array-ii_7449547
# Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/