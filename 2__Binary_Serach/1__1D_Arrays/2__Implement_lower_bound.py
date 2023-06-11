# O(log(N)) TC | O(1) SC
# N -> Length of the sorted array

def lowerBound(arr, length, target) -> int:
    ansIdx = -1
    
    leftIdx, rightIdx = 0, length - 1
    midIdx = 0
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # maybe an answer
        if arr[midIdx] >= target:
            ansIdx = midIdx
            # search for a better possible answer
            rightIdx = midIdx - 1
        elif arr[midIdx] < target:
            leftIdx = midIdx + 1
    
    if ansIdx == -1:
        return length
    return ansIdx



# Link: https://www.codingninjas.com/codestudio/problems/lower-bound_8165382