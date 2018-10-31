class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        sum_map = [[0] * n] * m
        sum_map[0][0] = grid[0][0]
        for x in range(m):
            for y in range(n):
                if x == 0 and y == 0:
                    continue
                up = sum_map[x - 1][y] if x > 0 else float('inf')
                left = sum_map[x][y - 1] if y > 0 else float('inf')
                sum_map[x][y] = min(up, left) + grid[x][y]
        return sum_map[m-1][n-1]
