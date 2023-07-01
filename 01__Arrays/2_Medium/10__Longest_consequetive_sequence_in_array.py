# ---------------- Solution 1 (Soritng approach) ----------------
# O(N*log(N)) TC | O(1) SC

def longestConsecutive(nums):
    # edge case
    if len(nums) == 0:  return 0
    
    nums.sort()
    maxSequenceLength = float('-inf')
    
    currentSequenceLength = 1
    prevNum = nums[0]
    # track max sequence length
    for i in range(1, len(nums)):
        if nums[i] == prevNum:
            continue
        if nums[i] == prevNum + 1:
            currentSequenceLength += 1
        else:
            maxSequenceLength = max(currentSequenceLength, maxSequenceLength)
            currentSequenceLength = 1
        # prevNum is updated anyways
        prevNum = nums[i]
    
    # consider the possibility of the last sequence
    maxSequenceLength = max(currentSequenceLength, maxSequenceLength)

    return maxSequenceLength



# ---------------- Solution 2 (Hashing approach) ----------------
# O(N) TC | O(N) SC

def longestConsecutive(nums):
    # edge case
    if len(nums) == 0:  return 0

    # store the numbers in a hashset
    numSet = set()
    for num in nums:
        numSet.add(num)
    
    longestSequenceLength = float('-inf')

    # check possible consequetive sequences
    for num in nums:
        prevNum = num - 1

        if prevNum not in numSet:
            nextNum = num + 1
            currentSequenceLength = 1
            # track the current sequence length
            while nextNum in numSet:
                currentSequenceLength += 1
                nextNum = nextNum + 1
            
            # update max length if needed
            longestSequenceLength = max(currentSequenceLength, longestSequenceLength)
    
    return longestSequenceLength



# Leetcode: https://leetcode.com/problems/longest-consecutive-sequence/
# GFG: https://practice.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/0
# CN: https://www.codingninjas.com/codestudio/problems/longest-successive-elements_6811740