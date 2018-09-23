# 7 2
# 1 2 3 -2 3 -10 3
x, y = input().strip().split()
x = int(x)
y = int(y)

data = input().strip().split()
data = list(map(int, data))
data = [0]+data
def MaxSum(m, n):
    if m<1 or n<m:
        return 0
    dp = list([0]*(x+1))
    past = list([0]*(x+1))
    for i in range(1, m+1):
        dp[i] = past[i-1] + data[i]
        _max = dp[i]
        for j in range(i+1, n-m+i+1):
            dp[j] = (dp[j-1] if dp[j-1] > past[j-1] else past[j-1])+data[j]
            past[j-1] = _max
            if _max < dp[j]:
                _max = dp[j]
        past[n-m+i] = _max
    ans = dp[0]
    for i in range(m, n+1):
        if dp[i] > ans:
            ans = dp[i]
    return ans

print(MaxSum(y, x))