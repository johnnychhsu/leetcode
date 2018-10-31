"""
This method take O(m*n) time and O(m) space
"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        ans = [0] * m
        ans[0] = grid[0][0]
        for i in range(1, m):
            ans[i] = ans[i - 1] + grid[i][0]
        for y in range(1, n):
            ans[0] += grid[0][y]
            for x in range(1, m):
                ans[x] = min(ans[x], ans[x - 1]) + grid[x][y]
        return ans[-1]
