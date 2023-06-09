# ------ Two Pointer approach ------
# O(N) TC | O(1) SC

def longestSubarrayWithSumK(a, k):
    arrayLen = len(a)

    maxSubarrayLength = 0
    currentSubarraySum = 0

    # sliding window method for finding sum
    start, end = 0, 0
    while start < arrayLen:
        # iterate till we exceed given sum
        while end < arrayLen and currentSubarraySum + a[end] <= k:
            currentSubarraySum += a[end]
            end += 1
        # check if we found the required sum
        if currentSubarraySum == k:
            currentSubarrayLength = end - start
            maxSubarrayLength = max(currentSubarrayLength, maxSubarrayLength)
        # slide the window
        currentSubarraySum -= a[start]
        start += 1
    
    return maxSubarrayLength



# Link: https://www.codingninjas.com/codestudio/problems/longest-subarray-with-sum-k_6682399