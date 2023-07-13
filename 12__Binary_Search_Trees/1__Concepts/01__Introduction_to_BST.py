# O(N) TC | O(1) SC     [N -> Length of array]

def isValidBST(inOrder):
    # check if the inOrder array is sorted in increasing fashion or not
    isValid = True
    for i in range(1, len(inOrder)):
        if inOrder[i] <= inOrder[i - 1]:
            isValid = False
            break
    
    return isValid



# CN: https://www.codingninjas.com/studio/problems/binary-search-trees_8160443