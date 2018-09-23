import sys
def solve(sets, sum):
    row = len(sets) + 1
    col = sum + 1
    solutionMatrix = [[0 for c in range(col)] for r in range(row)]
    solutionMatrix[0][0] = 1
    for i in range(1, col):
        solutionMatrix[0][i] = 0

    for j in range(1, row):
        solutionMatrix[j][0] = 1
        for k in range(1, col):
            solutionMatrix[j][k] = solutionMatrix[j - 1][k]
            if solutionMatrix[j][k] == 1:
                solutionMatrix[j][k] = solutionMatrix[j][k]
            elif (k - sets[j - 1] >= 0) and (solutionMatrix[j][k - sets[j - 1]] == 1):
                solutionMatrix[j][k] = solutionMatrix[j][k - sets[j - 1]]
            else:
                solutionMatrix[j][k] = 0
            if k == col - 1 and solutionMatrix[j][k] == 1:
                return 1
    return 0
if __name__=="__main__":
    m=int(sys.stdin.readline().strip())
    y=sys.stdin.readline().strip()
    data=list(map(int,y.split()))
    n=int(sys.stdin.readline().strip())
    res=solve(data,n)
    print(res)