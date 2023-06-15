# -------------- Sorting ----------
# O(NlogN) TC | O(N) SC
def largestElement(array) -> int:
    array.sort()
    return array[-1]


# ---------- Optimal Solution -----------
# O(N) TC | O(1) SC
def largestElement(array) -> int:
    maxVal = float('-inf')
    for num in array:
        maxVal = max(num, maxVal)
    
    return maxVal



# GFG: https://practice.geeksforgeeks.org/problems/largest-element-in-array4009/0
# CN: https://www.codingninjas.com/codestudio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279