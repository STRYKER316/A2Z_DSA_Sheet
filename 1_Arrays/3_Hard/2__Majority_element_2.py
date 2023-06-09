# ------- Optimal Approach (Moore's Voting Algorithm) -------
# O(N) TC | O(1) SC

def majorityElement(array):
    majorityNumber1, count1 = None, 0
    majorityNumber2, count2 = None, 0

    # voting algortihm
    for num in array:
        if num == majorityNumber1:
            count1 += 1
        elif num == majorityNumber2:
            count2 += 1
        elif majorityNumber1 == None or count1 == 0:
            majorityNumber1 = num
            count1 = 1
        elif majorityNumber2 == None or count2 == 0:
            majorityNumber2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    # verify the majority numbers
    majorityCount1, majorityCount2 = 0, 0
    for num in array:
        if num == majorityNumber1:  majorityCount1 += 1
        elif num == majorityNumber2: majorityCount2 += 1
    
    ans = []
    if majorityCount1 > len(array) // 3:
        ans.append(majorityNumber1)
    if majorityCount2 > len(array) // 3:
        ans.append(majorityNumber2)
    
    # sort the answer
    if len(ans) == 2 and ans[0] > ans[1]:
        ans[0], ans[1] = ans[1], ans[0]
    return ans



# Link: https://www.codingninjas.com/codestudio/problems/majority-element_6915220
# Link: https://leetcode.com/problems/majority-element-ii/