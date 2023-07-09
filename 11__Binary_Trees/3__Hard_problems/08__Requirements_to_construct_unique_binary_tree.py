# O(1) TC | O(1) SC
def uniqueBinaryTree(a, b):
    # preOrder -> 1, inOrder -> 2, postOrder -> 3
    if a == 2 and b == 2:   return False
    if a == 2 or b == 2:    return True


# CN: https://www.codingninjas.com/studio/problems/unique-binary-tree_8180906