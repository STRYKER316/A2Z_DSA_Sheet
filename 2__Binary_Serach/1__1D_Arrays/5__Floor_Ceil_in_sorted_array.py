# O(log(arrayLen)) TC | O(1) SC

def ceilingInSortedArray(arr, arrayLen, target):
    floorVal = -1
    ceilVal = -1

    leftIdx, rightIdx = 0, arrayLen - 1
    midIdx = 0
    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2
        # condition check
        if arr[midIdx] == target:
            floorVal = arr[midIdx]
            ceilVal = arr[midIdx]
            break
        elif arr[midIdx] < target:
            floorVal = arr[midIdx]
            leftIdx = midIdx + 1
        elif arr[midIdx] > target:
            ceilVal = arr[midIdx]
            rightIdx = midIdx - 1

    return [floorVal, ceilVal]



# CN: https://www.codingninjas.com/codestudio/problems/ceiling-in-a-sorted-array_1825401
# GFG: https://practice.geeksforgeeks.org/problems/ceil-the-floor2802/1