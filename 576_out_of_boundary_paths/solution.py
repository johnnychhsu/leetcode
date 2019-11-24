class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[i][j] = 1
        ans = 0
        for _ in range(N):
            tmp = [[0 for _ in range(n)] for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        cx = x + dx
                        cy = y + dy
                        if 0 <= cx < m and 0 <= cy < n:
                            tmp[cx][cy] = (dp[x][y] + tmp[cx][cy]) % 1000000007
                        else:
                            ans = (ans + dp[x][y]) % 1000000007
            dp = tmp
        return ans
                            
                            
