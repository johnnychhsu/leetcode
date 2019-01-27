class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
        prev = costs[0]
        for i in range(1, len(costs)):
            cur = [0 for x in range(len(costs[0]))]
            for j in range(len(costs[0])):
                cur[j] = costs[i][j] + min(prev[0:j] + prev[j+1:])
            prev = cur
        return min(prev)
        
        
