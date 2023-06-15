# O(log(number)) TC | O(1) SC

def floorSqrt(self, x): 
    possibleSquareRoot = 0
    
    start, end = 0, x
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        # check for square root
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            possibleSquareRoot = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return possibleSquareRoot



# GFG: https://practice.geeksforgeeks.org/problems/square-root/0