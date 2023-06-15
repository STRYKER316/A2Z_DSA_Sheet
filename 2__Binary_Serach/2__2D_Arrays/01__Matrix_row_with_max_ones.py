# O(R + C) TC | O(1) SC
# R -> RowCount, C -> ColumnCount

def rowWithMax1s(self, arr, n, m):
    ansRow = -1
    
    row, col = 0, m - 1
    while row < n and col >= 0:
        if arr[row][col] == 0:
            row += 1
        elif arr[row][col] == 1:
            ansRow = row
            col -= 1
    
    return ansRow



# GFG: https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1