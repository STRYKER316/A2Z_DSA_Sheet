# ------- Optimal Approach (Moore's Voting Algorithm) -------
# O(N) TC | O(1) SC

def majorityElement(array):
    majorityNumber = None
    majorityCount = 0
    for num in array:
        if num == majorityNumber:
            majorityCount += 1
        elif majorityCount == 0:
            majorityNumber = num
            majorityCount = 1
        else:
            majorityCount -= 1
    
    # verify the majority element
    actualCount = 0
    for num in array:
        if num == majorityNumber:
            actualCount += 1
    
    if actualCount > len(array) // 2:
        return majorityNumber
    return -1


# Link: https://bit.ly/3SSpeA3
# Link: https://leetcode.com/problems/majority-element/