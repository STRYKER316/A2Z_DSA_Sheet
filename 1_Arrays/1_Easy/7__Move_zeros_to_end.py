# O(N) TC | O(1) SC

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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



# Link: https://bit.ly/3PrGIjT
# Link: https://leetcode.com/problems/move-zeroes/