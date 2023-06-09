# O(N) TC | O(1) SC

def findMaxConsecutiveOnes(nums):
        maxConsequetiveCount = 0
        currentConsequetiveCount = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                currentConsequetiveCount += 1
            else:
                maxConsequetiveCount = max(maxConsequetiveCount, currentConsequetiveCount)
                currentConsequetiveCount = 0
        # check for a trailing subarray
        maxConsequetiveCount = max(maxConsequetiveCount, currentConsequetiveCount)

        return maxConsequetiveCount



# Link: https://leetcode.com/problems/max-consecutive-ones/