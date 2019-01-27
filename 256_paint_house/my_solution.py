class Solution:
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        dp = [[0 for x in range(3)] for x in range(len(costs))]
        dp[0] = costs[0]
        for i in range(1, len(costs)):
            for x in range(3):
                dp[i][x] = costs[i][x] + min(dp[i-1][0:x] + dp[i - 1][x + 1:])
        return min(dp[len(costs) - 1])

