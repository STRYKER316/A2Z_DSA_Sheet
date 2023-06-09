# ---------- Kadane's Algorithm ---------
# O(N) TC | O(1) SC

def maxSubArray(nums):
    globalMaxSubarraySum = float('-inf')
    runningSubarraySum = 0

    ansStartIdx, ansEndIdx = 0, 0
    currentStartIdx = 0
    for i in range(len(nums)):
        runningSubarraySum += nums[i]
        # update answer if needed
        if runningSubarraySum > globalMaxSubarraySum:
            globalMaxSubarraySum = runningSubarraySum
            ansStartIdx = currentStartIdx
            ansEndIdx = i
        # update start index if needed
        if runningSubarraySum < 0:
            runningSubarraySum = 0
            currentStartIdx = i + 1

    return nums[ansStartIdx : ansEndIdx + 1]



# Link: 