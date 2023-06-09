# O(N) TC | O(1) SC

def leftRotateOnce(arr):
    arrayLen = len(arr)

    # store the first element of array in a variable
    temp = arr[0]
    # left rotate other indices by one
    for i in range(1, len(arr)):
        arr[i - 1] = arr[i]
    # assign the value of variable at the last index
    arr[arrayLen - 1] = temp

    return
