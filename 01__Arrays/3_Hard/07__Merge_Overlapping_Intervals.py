# O(Nlog(N)) TC | O(1) SC       [N -> Number of intervals]

def merge(intervals):
    # sort the intervals
    intervals.sort()
    
    mergedIntervals = []
    mergedIntervals.append(intervals[0])

    for i in range(1, len(intervals)):
        previousInterval = mergedIntervals[-1]
        currentInterval = intervals[i]
        # check overlapping or not
        if previousInterval[1] < currentInterval[0]:
            mergedIntervals.append(currentInterval)
        else:
            previousInterval[1] = max(previousInterval[1], currentInterval[1])
    
    return mergedIntervals



# Leetcode: https://leetcode.com/problems/merge-intervals/
# GFG: https://practice.geeksforgeeks.org/problems/8a644e94faaa94968d8665ba9e0a80d1ae3e0a2d/1
# CN: https://www.codingninjas.com/codestudio/problems/merge-all-overlapping-intervals_6783452