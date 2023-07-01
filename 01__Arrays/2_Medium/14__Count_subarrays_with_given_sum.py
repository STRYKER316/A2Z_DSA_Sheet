# O(N) TC | O(N) SC     [N-> Length of array]

def subarraySum(nums, k):
    # record how many times a prefixSum value repeats
    prefixSumCountMap = {}

    subarrayCount = 0
    runningPrefixSum = 0
    for i in range(len(nums)):
        runningPrefixSum += nums[i]
        # case 1
        if runningPrefixSum == k:
            subarrayCount += 1
        # case 2
        requiredSum = runningPrefixSum - k
        if requiredSum in prefixSumCountMap:
            subarrayCount += prefixSumCountMap[requiredSum]
        
        # record the prefix sum
        prefixSumCountMap[runningPrefixSum] = prefixSumCountMap.get(runningPrefixSum, 0) + 1
    
    return subarrayCount



# Leetcoe: https://leetcode.com/problems/subarray-sum-equals-k/
# CN: https://www.codingninjas.com/codestudio/problems/subarray-sums-i_1467103