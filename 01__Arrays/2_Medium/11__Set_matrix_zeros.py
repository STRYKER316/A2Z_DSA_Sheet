# ------------- Solution 1 -----------
# O(N * M) TC | O(N + M) SC

def setZeroes(matrix):
    rowCount, colCount = len(matrix), len(matrix[0])

    # arrays to keep track of which row/col has a zero in the input matrix
    rowMarkArray = [1 for _ in range(rowCount)]
    colMarkArray = [1 for _ in range(colCount)]

    # track which row and col have o in the input matrix
    for row in range(rowCount):
        for col in range(colCount):
            if matrix[row][col] == 0:
                rowMarkArray[row] = 0
                colMarkArray[col] = 0

    # convert row and col of input matrix to 0s where needed
    for row in range(rowCount):
        for col in range(colCount):
            if rowMarkArray[row] == 0:
                matrix[row][col] = 0
            elif colMarkArray[col] == 0:
                matrix[row][col] = 0

    return matrix



# ------------- Solution 2 -----------
# O(N * M) TC | O(1) SC

def setZeroes(matrix):
    rowCount = len(matrix)
    colCount = len(matrix[0])

    columnZeroStatus = 1
    # 1> mark the first element of the row and col as 0, when we encounter a 0 cell
    for i in range(rowCount):
        for j in range(colCount):
            if matrix[i][j] == 0:
                # mark i-th row
                matrix[i][0] = 0
                # mark j-th column
                if j != 0:  matrix[0][j] = 0
                else:   columnZeroStatus = 0

    # 2> modify the matrix, starting from 2nd row and 2nd column, based on info stored in 1st row and 1st col
    for i in range(1, rowCount):
        for j in range(1, colCount):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
    
    # 3> modify the 1st row, if needed
    if matrix[0][0] == 0:
        for j in range(colCount):
            matrix[0][j] = 0
    
    # 4> modify the 1st col, if needed
    if columnZeroStatus == 0:
        for i in range(rowCount):
            matrix[i][0] = 0
    
    return



# Leetcode: https://leetcode.com/problems/set-matrix-zeroes/
# CN: https://www.codingninjas.com/codestudio/problems/zero-matrix_1171153
# GFG: https://practice.geeksforgeeks.org/problems/make-zeroes4042/1