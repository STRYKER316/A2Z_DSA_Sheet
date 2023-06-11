# O(log(arrayLen)) | O(1) SC

def upperBound(arr, target, arrayLen) -> int:
    ansIdx = -1

    leftIdx, rightIdx = 0, arrayLen - 1
    midIdx = 0
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # maybe an asnwer
        if arr[midIdx] > target:
            ansIdx = midIdx
            # search for a better possible answer
            rightIdx = midIdx - 1
        elif arr[midIdx] <= target:
            leftIdx = midIdx + 1
    
    if ansIdx == -1:
        return arrayLen
    return ansIdx



# Link: https://www.codingninjas.com/codestudio/problems/implement-upper-bound_8165383