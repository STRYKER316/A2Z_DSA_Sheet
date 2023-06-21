# --------------- Solution 1 (Sorting after swapping) --------------
# O(NlogN + MlogM) TC | O(1) SC     [N -> length of array1, M -> Length of array2]

def merge(arr1, arr2):
    arrayLen1, arrayLen2 = len(arr1), len(arr2)

    leftIdx = arrayLen1 - 1
    rightIdx = 0
    while leftIdx >= 0 and rightIdx < arrayLen2:
        if arr1[leftIdx] > arr2[rightIdx]:
            arr1[leftIdx], arr2[rightIdx] = arr2[rightIdx], arr1[leftIdx]
            leftIdx -= 1
            rightIdx += 1
        else: break
    
    arr1.sort()
    arr2.sort()
    return


# --------------- Solution 2 (Gap Method) --------------
# O((N + M)log(N + M)) TC | O(1) SC     [N -> length of array1, M -> Length of array2]

def merge(arr1,arr2):
    arrayLen1, arrayLen2 = len(arr1), len(arr2)
    totalLength = arrayLen1 + arrayLen2
    
    # declare the initial value for gap
    gap = (totalLength // 2) + (totalLength % 2)
    while gap >= 1:
        leftIdx = 0
        rightIdx = leftIdx + gap
        
        while rightIdx < totalLength:
            # case1
            if leftIdx < arrayLen1 and rightIdx < arrayLen1:
                idx1 = leftIdx
                idx2 = rightIdx
                if arr1[idx1] > arr1[idx2]:
                    swap(arr1, arr1, idx1, idx2)
            
            # case2
            elif leftIdx < arrayLen1 and rightIdx >= arrayLen1:
                idx1 = leftIdx
                idx2 = rightIdx - arrayLen1
                if arr1[idx1] > arr2[idx2]:
                    swap(arr1, arr2, idx1, idx2)
            
            # case3
            elif leftIdx >= arrayLen1 and rightIdx >= arrayLen1:
                idx1 = leftIdx - arrayLen1
                idx2 = rightIdx - arrayLen1
                if arr2[idx1] > arr2[idx2]:
                    swap(arr2, arr2, idx1, idx2)
            
            # upadte
            leftIdx += 1
            rightIdx += 1
        
        # stop when iteration cmpletes for gap = 1
        if gap == 1:
            break
        # update gap for next iteration
        gap = (gap // 2) + (gap % 2)
    
    return

# Helper Method
def swap(array1, array2, leftIdx, rightIdx):
    array1[leftIdx], array2[rightIdx] = array2[rightIdx], array1[leftIdx]



# GFG: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
# CN: https://www.codingninjas.com/codestudio/problems/merge-two-sorted-arrays-without-extra-space_6898839
# Leetcode: https://leetcode.com/problems/merge-sorted-array/