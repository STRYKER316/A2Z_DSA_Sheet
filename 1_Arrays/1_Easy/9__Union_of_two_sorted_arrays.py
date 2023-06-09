# O(len1 + len2) TC | O(1) SC

def findUnion(arr1, arr2, len1, len2):
        unionList = []
        
        idx1, idx2 = 0, 0
        while idx1 < len1 and idx2 < len2:
            if arr1[idx1] <= arr2[idx2]:
                # push a[idx1]
                if len(unionList) == 0 or unionList[-1] != arr1[idx1]:
                    unionList.append(arr1[idx1])
                idx1 += 1
            else:
                # push b[idx2]
                if len(unionList) == 0 or unionList[-1] != arr2[idx2]:
                    unionList.append(arr2[idx2])
                idx2 += 1
        
        # append the remaining elements
        for i in range(idx1, len1):
            if unionList[-1] != arr1[i]:
                unionList.append(arr1[i])
        for j in range(idx2, len2):
            if unionList[-1] != arr2[j]:
                unionList.append(arr2[j])
        
        return unionList



# Link: https://bit.ly/3Ap7Onp