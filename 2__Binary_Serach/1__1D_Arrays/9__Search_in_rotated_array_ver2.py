# O(log(n)) TC | O(1) SC -> Average Case
# O(n/2) TC | O(1) SC -> Worst Case

def Search(n, arr, k):
    leftIdx, rightIdx = 0, n - 1
    midIdx = 0

    while leftIdx <= rightIdx:
        midIdx = (leftIdx + rightIdx) // 2

        left = arr[leftIdx]
        right = arr[rightIdx]
        mid = arr[midIdx]

        if arr[midIdx] == k:
            return 1
        # check fr duplicate numbers
        if arr[leftIdx] == arr[midIdx] and arr[midIdx] == arr[rightIdx]:
            leftIdx += 1
            rightIdx -= 1
        # check if left-half is sorted or not
        elif arr[leftIdx] <= arr[midIdx]:
            if arr[leftIdx] <= k and k <= arr[rightIdx]:
                rightIdx = midIdx - 1
            else:   leftIdx = midIdx + 1
        # right-half is sorted
        else:
            if arr[midIdx] <= k and k <= arr[rightIdx]:
                leftIdx = midIdx + 1
            else:   rightIdx = midIdx - 1
    
    return 0



# GFG: https://bit.ly/3Rm85Nb
# CN: https://www.codingninjas.com/codestudio/problems/search-in-a-rotated-sorted-array-ii_7449547
# Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/