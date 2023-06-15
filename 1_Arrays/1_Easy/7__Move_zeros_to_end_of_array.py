# O(N) TC | O(1) SC

def moveZeroes(nums):
        # find the index of first 0
        currentZeroIdx = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                currentZeroIdx = i
                break
        # if not one 0 was found
        if currentZeroIdx == -1:    return nums
        
        # swap immediate non-zero values with the current zero
        for j in range(currentZeroIdx + 1, len(nums)):
            if nums[j] != 0:
                nums[currentZeroIdx], nums[j] = nums[j], nums[currentZeroIdx]
                currentZeroIdx += 1
        
        return



# GFG: https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
# Leetcode: https://leetcode.com/problems/move-zeroes/
# CN: https://www.codingninjas.com/codestudio/problems/ninja-and-the-zero-s_6581958