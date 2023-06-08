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
