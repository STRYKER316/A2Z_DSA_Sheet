# O(rowCount * colCount) TC | O(1) SC

def spiralOrder(matrix):
    # declare corner points
    topRow = 0
    bottomRow = len(matrix) - 1
    leftCol = 0
    rightCol = len(matrix[0]) - 1

    spiralTraversal = []
    # traverse layer by layer
    while topRow <= bottomRow and leftCol <= rightCol:
        # traverse top (leftCol -> rightCol)
        for j in range(leftCol, rightCol + 1):
            spiralTraversal.append(matrix[topRow][j])
        
        # traverse right (topRow + 1 -> bottomRow - 1)
        for i in range(topRow + 1, bottomRow):
            spiralTraversal.append(matrix[i][rightCol])

        # traverse bottom (rightCol -> leftCol)
        if topRow != bottomRow:
            for j in range(rightCol, leftCol - 1, -1):
                spiralTraversal.append(matrix[bottomRow][j])

        # traverse left (bottomRow - 1 -> topRow + 1)
        if leftCol != rightCol:
            for i in range(bottomRow - 1, topRow, -1):
                spiralTraversal.append(matrix[i][leftCol])

        # update corner points for next iteration
        topRow += 1
        bottomRow -= 1
        leftCol += 1
        rightCol -= 1
    
    return spiralTraversal



# Leetcoe: https://leetcode.com/problems/spiral-matrix/
# CN: https://www.codingninjas.com/codestudio/problems/spiral-matrix_6922069
# GFG: https://practice.geeksforgeeks.org/problems/cd61add036272faa69c6814e34aa7007d5a25aa6/1