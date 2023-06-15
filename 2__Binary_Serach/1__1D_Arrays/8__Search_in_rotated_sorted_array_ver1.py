# O(log(n)) TC | O(1) SC

def search(arr, n, k):
	# k -> target, n -> arrayLen
	leftIdx, rightIdx = 0, n - 1
	midIdx = 0

	ansIdx = -1
	while leftIdx <= rightIdx:
		midIdx = (leftIdx + rightIdx) // 2

		if arr[midIdx] == k:
			ansIdx = midIdx
			break
		# check if left-half is sorted or not
		elif arr[leftIdx] <= arr[midIdx]:
			if arr[leftIdx] <= k and k <= arr[midIdx]:
				rightIdx = midIdx - 1
			else:   leftIdx = midIdx + 1
		# check if right-half is sorted or not
		elif arr[rightIdx] >= arr[midIdx]:
			if arr[midIdx] <= k and k <= arr[rightIdx]:
				leftIdx = midIdx + 1
			else:   rightIdx = midIdx - 1
	
	return ansIdx


# GFG: https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array4618/1
# CN: https://www.codingninjas.com/codestudio/problems/search-in-rotated-sorted-array_1082554
# Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/