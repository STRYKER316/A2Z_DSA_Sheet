# O(N) TC | O(1) SC

def singleNumber(nums):
        arrayXor = 0
        for num in nums:
            arrayXor ^= num
        
        return arrayXor



# Link: https://leetcode.com/problems/single-number/