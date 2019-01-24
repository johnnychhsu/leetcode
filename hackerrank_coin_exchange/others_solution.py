def getWays(n, c):
    if not c:
        return 0
    dp = [[0 for i in range(len(c))] for x in range(n+1)]
    for i in range(len(c)):
        dp[0][i] = 1
    for i in range(1, n+1):
        for j in range(len(c)):
            x = dp[i - c[j]][j] if i - c[j] >= 0 else 0
            y = dp[i][j - 1] if j - 1 >= 0 else 0
            dp[i][j] = x + y
    return dp[n][len(c) - 1]

c = [1,2,3]
n = 4
print(getWays(n, c))
