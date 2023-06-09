# O(N) TC | O(1) SC

def linearSearch(array, num):
    for i in range(len(array)):
        if array[i] == num:
            return i
    return -1

