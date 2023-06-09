# O(N) TC | O(1) SC

def arraySortedOrNot(self, arr, n):
    isSorted = True
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            isSorted = False
            break
    
    return isSorted



# Link: https://bit.ly/3Ap9U6F