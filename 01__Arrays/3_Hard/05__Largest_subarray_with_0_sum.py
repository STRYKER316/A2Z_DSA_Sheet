# O(N) TC | O(N) SC     [N -> Length of array]

def maxLen(arr, n):
    prefixSumIndexMap = {}
    maxLengthSubarray = 0
    
    runningPrefixSum = 0
    for i in range(n):
        runningPrefixSum += arr[i]
        
        # case 1
        if runningPrefixSum == 0:
            currentSubarrayLength = i + 1
            maxLengthSubarray = max(currentSubarrayLength, maxLengthSubarray)
        
        # case 2
        if runningPrefixSum in prefixSumIndexMap:
            currentSubarrayLength = i - prefixSumIndexMap[runningPrefixSum]
            maxLengthSubarray = max(currentSubarrayLength, maxLengthSubarray)
        
        # record the prefixSum
        if runningPrefixSum not in prefixSumIndexMap:
            prefixSumIndexMap[runningPrefixSum] = i
    
    return maxLengthSubarray



# GFG: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1