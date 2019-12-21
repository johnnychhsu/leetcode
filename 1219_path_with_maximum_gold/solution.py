class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def isValid(x, y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            else:
                return False
        
        def find(x, y):
            if isValid(x, y) and not visited[x][y] and grid[x][y] != 0:
                visited[x][y] = 1
                cur = grid[x][y]
                tmp = 0
                for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    nx = x + dx
                    ny = y + dy
                    tmp = max(tmp, find(nx, ny))
                visited[x][y] = 0
                return cur + tmp
            else:
                return 0
                
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] != 0:
                    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
                    ans = max(ans, find(x, y))
        return ans
