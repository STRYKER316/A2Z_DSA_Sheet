# O(N) TC | O(1) SC

def singleNumber(nums):
        arrayXor = 0
        for num in nums:
            arrayXor ^= num
        
        return arrayXor



# GFG: https://practice.geeksforgeeks.org/problems/element-appearing-once2552/0
# Leetcode: https://leetcode.com/problems/single-number/
# CN: https://www.codingninjas.com/codestudio/problems/find-the-single-element_6680465