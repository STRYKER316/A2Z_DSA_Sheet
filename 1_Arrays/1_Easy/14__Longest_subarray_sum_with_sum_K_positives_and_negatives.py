# --------- HashMap approach ---------
# O(N) TC | O(N) SC
 
def lenOfLongSubarr (arr, k) : 
    sumTillIndexMap = {}
    maxLengthSubarray = 0

    runningSum = 0
    for i in range(len(arr)):
        # record the sum till current index
        runningSum += arr[i]
        if runningSum not in sumTillIndexMap:
            sumTillIndexMap[runningSum] = i

        # case 1
        if runningSum == k:
            currentLength = i + 1
            maxLengthSubarray = max(maxLengthSubarray, currentLength)
        # case 2
        requiredSum = runningSum - k
        if requiredSum in sumTillIndexMap:
            currentLength = i - sumTillIndexMap[requiredSum]
            maxLengthSubarray = max(maxLengthSubarray, currentLength)
    
    return maxLengthSubarray



# GFG: https://practice.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
# CN: https://www.codingninjas.com/codestudio/problems/longest-subarray-with-sum-k_5713505