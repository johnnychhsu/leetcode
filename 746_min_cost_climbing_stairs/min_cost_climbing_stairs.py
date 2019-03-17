class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        top = len(cost)
        dp = [-1 for _ in range(top)]
        dp[0] = cost[0]
        dp[1] = cost[1]

        def find(i):
            if i == 0:
                return cost[0]
            elif i == 1:
                return cost[1]
            elif dp[i] != -1:
                return dp[i]
            else:
                dp[i] = min(find(i - 1), find(i - 2)) + cost[i]
                return dp[i]

        return find(top - 1)
