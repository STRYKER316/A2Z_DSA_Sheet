def twoSum(nums, target):
    numberAndIndexMap = {}
    ans = [-1, -1]

    for i in range(len(nums)):
        currentNum = nums[i]
        complementNum = target - currentNum
        if complementNum in numberAndIndexMap:
            ans[0] = numberAndIndexMap[complementNum]
            ans[1] = i
            break
        else:   numberAndIndexMap[currentNum] = i
    
    return ans



# Link: https://leetcode.com/problems/two-sum/