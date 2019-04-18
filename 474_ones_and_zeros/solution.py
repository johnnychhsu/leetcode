class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def countBit(s):
            ones = 0
            zeros = 0
            for w in s:
                if w == "1":
                    ones += 1
                else:
                    zeros += 1
            return ones, zeros
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for s in strs:
            ones, zeros = countBit(s)
            for x in range(m, zeros-1, -1):
                for y in range(n, ones-1, -1):
                    dp[x][y] = max(dp[x][y], 1 + dp[x-zeros][y-ones])
        return dp[m][n]
