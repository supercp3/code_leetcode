import sys
import numpy as np

def solve(S, n, M):
    subset = np.array([[True]*(M+1)]*(n+1))
    for i in range(0, n+1):
        subset[i, 0] = True

    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, M+1):
        subset[0, i] = False

    # Fill the subset table in bottom-up manner
    for i in range(1, n+1):
        for j in range(1, M+1):
            if j < S[i-1]:
                subset[i, j] = subset[i-1, j]
            else:
                subset[i, j] = subset[i-1, j] or subset[i-1, j-S[i-1]]

    # print the True-False table
    for i in range(0, n+1):
        for j in range(0, M+1):
            print('%-6s'%subset[i][j], end="  ")
        print(" ")

    if subset[n, M]:
        print("Found a subset with given sum")
        sol = []
        # using backtracing to find the solution
        i = n
        while i >= 0:
            if subset[i, M] and not subset[i-1, M]:
                sol.append(S[i-1])
                M -= st[i-1]
            if M == 0:
                break
            i -= 1
        print('The solution is %s.' % sol)
    else:
        print("No subset with given sum")

if __name__=="__main__":
    m=int(sys.stdin.readline().strip())
    y=sys.stdin.readline().strip()
    data=list(map(int,y.split()))
    n=int(sys.stdin.readline().strip())
    res=solve(data,m,n)
    print(res)
# test
#st = [1, 3, 4, 5]
#n = len(st)
#sm = 7
#isSubsetSum(st, n, sm)