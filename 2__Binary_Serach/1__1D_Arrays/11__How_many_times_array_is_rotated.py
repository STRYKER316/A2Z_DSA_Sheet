# O(log(arrayLen)) TC | O(1) SC

def findKRotation(self,arr,  n):
    # no rotation check
    if arr[0] < arr[-1]:    return 0
    
    minValue, minValueIdx = float('inf'), -1
    leftIdx, rightIdx = 0, n - 1
    midIdx = 0
    
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # check if left half is sorted
        if arr[leftIdx] <= arr[midIdx]:
            if arr[leftIdx] < minValue:
                minValue = arr[leftIdx]
                minValueIdx = leftIdx
            leftIdx = midIdx + 1
        # else right half is sorted
        elif arr[midIdx] <= arr[rightIdx]:
            if arr[midIdx] < minValue:
                minValue = arr[midIdx]
                minValueIdx = midIdx
            rightIdx = midIdx - 1
    
    # rotation count is the distance of minValueIdx from start of the array
    return minValueIdx



# GFG: https://practice.geeksforgeeks.org/problems/rotation4723/1
# CN: https://www.codingninjas.com/codestudio/problems/rotation_7449070