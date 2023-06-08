# ------------- Dutch National Flag Algortihm ----------
# O(N) TC | O(1) SC

def sort012(array):
    # [0, low - 1]      => 0s
    # [low, mid - 1]    => 1s
    # [mid, high]       => unsorted
    # [high + 1, n - 1] => 2s
    low = 0
    mid = 0
    high = len(array) - 1
    
    while mid <= high:
        if array[mid] == 0:
            swap(array, low, mid)
            low += 1
            mid += 1
        elif array[mid] == 1:
            mid += 1
        elif array[mid] == 2:
            swap(array, mid, high)
            high -= 1
    
    return array


# Helper Method
def swap(array, leftIdx, rightIdx):
    array[leftIdx], array[rightIdx] = array[rightIdx], array[leftIdx]



# Link: https://bit.ly/3dsROaZ