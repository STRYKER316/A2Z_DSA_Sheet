# O(N^2) TC | O(1) SC
# N -> Square Matrix row/col count

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    matrixTranspose(matrix)
    matrixMirrorImage(matrix)
    return


# Helper Method1
def matrixTranspose(matrix):
    rowCount = len(matrix)
    colCount = len(matrix[0])

    for i in range(rowCount):
        for j in range(i + 1, colCount):
            # swap
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return


# Helper Method2
def matrixMirrorImage(matrix):
    rowCount = len(matrix)
    colCount = len(matrix[0])

    for i in range(rowCount):
        leftCol = 0 
        rightCol = colCount - 1
        while leftCol < rightCol:
            # swap
            matrix[i][leftCol], matrix[i][rightCol] = matrix[i][rightCol], matrix[i][leftCol]
            # update
            leftCol += 1
            rightCol -= 1
    return



# Leetcode: https://leetcode.com/problems/rotate-image/
# GFG: https://practice.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1
# CN: https://www.codingninjas.com/codestudio/problems/rotate-the-matrix_6825090