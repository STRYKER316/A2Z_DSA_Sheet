# O(N) TC | O(1) SC

def arraySortedOrNot(self, arr, n):
    isSorted = True
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            isSorted = False
            break
    
    return isSorted



# GFG: https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
# Leetcode: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
# CN: https://www.codingninjas.com/codestudio/problems/ninja-and-the-sorted-check_6581957