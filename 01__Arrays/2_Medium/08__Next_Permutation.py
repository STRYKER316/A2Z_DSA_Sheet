# O(arrayLen) TC | O(1) SC

def nextPermutation(nums):
    arrayLen = len(nums)
    
    # find the first decrement pint in numbers starting from end
    dipIdx = -1
    for i in range(arrayLen - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            dipIdx = i
            break
    # if no dip was found, it implies this is the last permutation
    if dipIdx == -1:
        reverseArray(nums, 0, arrayLen - 1)
        return nums
    
    # find the smallest number greater than the dip Value, on its right and swap those two
    for j in range(arrayLen - 1, dipIdx, -1):
        if nums[j] > nums[dipIdx]:
            swap(nums, j, dipIdx)
            break
    
    # reverse the right part of dipIdx, which will be the next permutation of the input
    reverseArray(nums, dipIdx + 1, arrayLen - 1)
    return nums



# Helper Method1
def reverseArray(array, leftIdx, rightIdx):
    while leftIdx < rightIdx:
        swap(array, leftIdx, rightIdx)
        leftIdx += 1
        rightIdx -= 1
    return

# Helper Method2
def swap(array, leftIdx, rightIdx):
    array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]



# GFG: https://practice.geeksforgeeks.org/problems/next-permutation5226/1
# Leetcode: https://leetcode.com/problems/next-permutation/
# CN: https://www.codingninjas.com/codestudio/problems/893046
