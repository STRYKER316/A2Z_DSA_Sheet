# O(N^3) TC | O(1) SC   [N-> Length of array]

def fourSum(nums, target):
    arrayLen = len(nums)

    nums.sort()
    uniqueQuads = []

    # fix the first value
    for firstIdx in range(arrayLen - 3):
        # skip duplicates for firstIdx, if there are any
        if firstIdx > 0 and nums[firstIdx] == nums[firstIdx - 1]:
            continue
        
        # fix the second value
        for secondIdx in range(firstIdx + 1, arrayLen - 2):
            # skip duplicates for secondIdx, if there are any
            if secondIdx > firstIdx + 1 and nums[secondIdx] == nums[secondIdx - 1]:
                continue

            # fix the third and fourth values
            thirdIdx, fourthIdx = secondIdx + 1, arrayLen - 1
            while thirdIdx < fourthIdx:
                currentSum = nums[firstIdx] + nums[secondIdx] + nums[thirdIdx] + nums[fourthIdx]
                # check for target
                if currentSum == target:
                    uniqueQuads.append([nums[firstIdx], nums[secondIdx], nums[thirdIdx], nums[fourthIdx]])
                    # skip duplicats for secondIdx and thirdIdx, if there are any
                    while thirdIdx < fourthIdx and nums[thirdIdx] == nums[thirdIdx + 1]:
                        thirdIdx += 1
                    while thirdIdx < fourthIdx and nums[fourthIdx] == nums[fourthIdx - 1]:
                        fourthIdx -= 1
                    # update
                    thirdIdx += 1
                    fourthIdx -= 1

                elif currentSum < target:
                    thirdIdx += 1
                
                elif currentSum > target:
                    fourthIdx -= 1
        
    return uniqueQuads


# Leetcode: https://leetcode.com/problems/4sum/
# GFG: https://practice.geeksforgeeks.org/problems/find-all-four-sum-numbers1732/1
# CN: https://www.codingninjas.com/codestudio/problems/4sum_5713771