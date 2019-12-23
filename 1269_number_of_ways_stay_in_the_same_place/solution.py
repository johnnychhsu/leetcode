class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [[-1 for _ in range(steps+1)] for _ in range(steps)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, steps):
            dp[i][0] = 0
        constraint = min(steps, arrLen)
        def find(index, res):
            if index < 0 or index >= constraint:
                return 0
            elif dp[index][res] != -1:
                return dp[index][res]
            elif res < index:
                dp[index][res] = 0
                return 0
            else:
                dp[index][res] = find(index, res-1) + find(index-1, res-1) + find(index+1, res-1)
                return dp[index][res]
        find(0, steps)
        return dp[0][steps] % 1000000007
            
        
