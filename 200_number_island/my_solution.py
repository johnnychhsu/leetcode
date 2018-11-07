class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        cache = set()
        count = 0

        h = len(grid)
        w = len(grid[0])
        
        def isValid(x, y):
            if 0 <= x < h and 0 <= y < w:
                return True
            else:
                return False
        
        def mark(x, y, grid):
            if isValid(x + 1, y) and (x + 1, y) not in cache and grid[x + 1][y] == '1':
                cache.add((x + 1, y))
                mark(x + 1, y, grid)
                
            if isValid(x - 1, y) and (x - 1, y) not in cache and grid[x - 1][y] == '1':
                cache.add((x - 1, y))
                mark(x - 1, y, grid)
                
            if isValid(x, y + 1) and (x, y + 1) not in cache and grid[x][y + 1] == '1':
                cache.add((x, y + 1))
                mark(x, y + 1, grid)
            
            if isValid(x, y - 1) and (x, y - 1) not in cache and grid[x][y - 1] == '1':
                cache.add((x, y - 1))
                mark(x, y - 1, grid)
                
        for x in range(h):
            for y in range(w):
                if (x, y) not in cache and grid[x][y] == '1':
                    count += 1
                    mark(x, y, grid)
                cache.add((x, y))
        return count
