# O(log(rowCount * colCount)) TC | O(1) SC

def searchMatrix(mat, target):
    rowCount = len(mat)
    colCount = len(mat[0])

    startIdx = 0
    endIdx = (rowCount * colCount) - 1
    midIdx = 0
    while startIdx <= endIdx:
        midIdx = (startIdx + endIdx) // 2
        row = midIdx // colCount
        col = midIdx % colCount
        # search for target
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            startIdx = midIdx + 1
        else:
            endIdx = midIdx - 1
    
    return False


# LeetCode: https://leetcode.com/problems/search-a-2d-matrix/
# CN: https://www.codingninjas.com/codestudio/problems/980531