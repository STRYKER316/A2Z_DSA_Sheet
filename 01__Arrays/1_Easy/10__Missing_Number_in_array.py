# ------------ XOR Approach --------
# O(N) TC | O(1) SC

def missingNumber(array, N):
    rangeXor = 0
    arrayXor = 0
    
    for i in range(N - 1):
        arrayXor ^= array[i]
        rangeXor ^= (i + 1)
    rangeXor ^= N
    
    missingNum = rangeXor ^ arrayXor
    return missingNum


# ------------ Range-Sum Approach --------
# O(N) TC | O(1) SC

def missingNumber(array, N):
    rangeSum = N * (N + 1) // 2
    
    ans = rangeSum
    for num in array:
        ans -= num
    
    return ans



# GFG: https://practice.geeksforgeeks.org/problems/missing-number4257/1
# Leetcode: https://leetcode.com/problems/missing-number/
# CN: https://www.codingninjas.com/codestudio/problems/missing-number_6680467