# ---------- Kadane's Algorithm ----------
# O(N) TC | O(1) SC

def maxSubArraySum(arr, N):
    # # ---------------- Approach 1 --------------------
    # globalMaxSubarraySum = float('-inf')
    # maxSubarraySumTillNow = 0
    
    # for num in arr:
    #     maxSubarraySumTillNow = max(maxSubarraySumTillNow + num, num)
    #     globalMaxSubarraySum = max(globalMaxSubarraySum, maxSubarraySumTillNow)
    
    # return globalMaxSubarraySum
    
    
    # ---------------- Approach 2 --------------------
    globalMaxSubarraySum = float('-inf')
    runningSubarraySum = 0
    
    for num in arr:
        runningSubarraySum += num
        globalMaxSubarraySum = max(globalMaxSubarraySum, runningSubarraySum)
        # reset if needed
        if runningSubarraySum < 0:
            runningSubarraySum = 0
    
    return globalMaxSubarraySum



# GFG: https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/0
# Leetcode: https://leetcode.com/problems/maximum-subarray/
# CN: https://www.codingninjas.com/codestudio/problems/maximum-subarray-sum_630526