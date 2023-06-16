# ----------- Version 1 (Eqaul number of positive and negatives) ---------------
# O(N) TC | O(N) SC

def rearrangeArray(nums):
    rearrangedArray = [0 for _ in range(len(nums))]
    posIdx, negIdx = 0, 1

    for num in nums:
        if num > 0:
            rearrangedArray[posIdx] = num
            posIdx += 2
        else:
            rearrangedArray[negIdx] = num
            negIdx += 2
    
    return rearrangedArray


# Leetcoe: https://leetcode.com/problems/rearrange-array-elements-by-sign/
# CN: https://www.codingninjas.com/codestudio/problems/alternate-numbers_6783445



# ----------- Version 2 (Non-eqaul number of positive and negatives) ---------------
# O(N) TC | O(N) SC

def rearrange(self,arr, n):
    # segrgate the positive and negative values
    positiveValues = []
    negativeValues = []
    for num in arr:
        if num >= 0:
            positiveValues.append(num)
        else:   negativeValues.append(num)
    
    rearrangedArray = [0 for _ in range(len(arr))]
    
    # put the values into rearrangedArray
    posArrayLen, negArrayLen = len(positiveValues), len(negativeValues)
    posIdx, negIdx = 0, 0
    currentIdx = 0
    # iterate till one of the arrays is completed
    while posIdx < posArrayLen and negIdx < negArrayLen:
        rearrangedArray[currentIdx] = positiveValues[posIdx]
        rearrangedArray[currentIdx + 1] = negativeValues[negIdx]
        # update
        posIdx += 1
        negIdx += 1
        currentIdx += 2
    
    # put the remaining elements into rearrangedAarray
    largerArray = positiveValues if len(positiveValues) > len(negativeValues) else negativeValues
    largerArrayIdx = posIdx if posIdx < posArrayLen else negIdx
    while largerArrayIdx < len(largerArray):
        rearrangedArray[currentIdx] = largerArray[largerArrayIdx]
        # upate
        largerArrayIdx += 1
        currentIdx += 1
    
    return rearrangeArray


# GFG: https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1
