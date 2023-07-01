# O(N^2) TC | O(1) SC   [N -> Length of array]

def threeSum(nums):
    arrayLen = len(nums)
    
    nums.sort()
    triplets = []

    firstIdx = 0
    while firstIdx <= arrayLen - 3:
        # choose the indices for remaining two numbers
        secondIdx = firstIdx + 1
        thirdIdx = arrayLen - 1

        while secondIdx < thirdIdx:
            firstNum, secondNum, thirdNum = nums[firstIdx], nums[secondIdx], nums[thirdIdx]

            # check target requirement
            if firstNum + secondNum + thirdNum == 0:
                triplets.append([firstNum, secondNum, thirdNum])
                # skip the duplicates for secondNum and thirdNum, if there are any
                while secondIdx < thirdIdx and nums[secondIdx] == nums[secondIdx + 1]:
                    secondIdx += 1
                while secondIdx < thirdIdx and nums[thirdIdx] == nums[thirdIdx - 1]:
                    thirdIdx -= 1
                # update
                secondIdx += 1
                thirdIdx -= 1
            
            elif firstNum + secondNum + thirdNum < 0:
                secondIdx += 1
            
            else:   thirdIdx -= 1
        
        # skip duplicates for firstIdx, if there are any
        while firstIdx < arrayLen - 3 and nums[firstIdx] == nums[firstIdx + 1]:
            firstIdx += 1
        # update
        firstIdx += 1
    
    return triplets



# Leetcode: https://leetcode.com/problems/3sum/
# CN: https://www.codingninjas.com/codestudio/problems/three-sum_6922132
# GFG: https://practice.geeksforgeeks.org/problems/3-sum-closest/1