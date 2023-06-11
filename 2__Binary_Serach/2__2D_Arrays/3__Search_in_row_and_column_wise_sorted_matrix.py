# O(R + C) TC | O(1) SC
# R -> RowCount, C -> ColumnCount

def search(matrix, x):
    rowCount, colCount = len(matrix), len(matrix[0])

    targetPosition = [-1, -1]
    row = 0
    col = colCount - 1
    while row < rowCount and col >= 0:
        if matrix[row][col] == x:
            targetPosition = [row, col]
            break
        elif matrix[row][col] < x:
            row += 1
        elif matrix[row][col] > x:
            col -= 1
    
    return targetPosition



# Link: https://www.codingninjas.com/codestudio/problems/search-in-a-row-wise-and-column-wise-sorted-matrix_839811
# Link: https://bit.ly/3dAwi3Z
# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/description/