# O(N) TC | O(1) SC

def leaders(self, A, N):
    currentLeader = A[-1]
    leaders = [currentLeader]
    
    for i in range(N - 2, -1, -1):
        if A[i] >= currentLeader:
            leaders.append(A[i])
            currentLeader = A[i]
    
    leaders.reverse()
    return leaders



# Link: https://bit.ly/3bZqbGc