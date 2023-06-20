# -------------- Approach1 (Range Sum) ------------
# O(N) TC | O(1) SC     [N -> Length of array]

def findMissingRepeatingNumbers(arr):
    # P => Twice, Q => Missing
    # difference => P - Q
    # SquaredDifference => P^2 - Q^2
    difference = 0
    squaredDifference = 0

    for i in range(len(arr)):
        difference += arr[i]
        difference -= (i + 1)

        squaredDifference += arr[i] ** 2
        squaredDifference -= (i + 1) ** 2
    
    addition = squaredDifference // difference
    # get the values
    repeatingValue = (addition + difference) // 2
    missingValue = addition - repeatingValue

    return [repeatingValue, missingValue]



# GFG: https://practice.geeksforgeeks.org/problems/find-missing-and-repeating2512/1
# CN: https://www.codingninjas.com/codestudio/problems/missing-and-repeating-numbers_6828164