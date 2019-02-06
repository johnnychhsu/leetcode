class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        if len(matrix) == 1:
            return int(max(matrix[0]))
        row = len(matrix)
        col = len(matrix[0])
        s = [[0 for _ in range(col)] for _ in range(row)]
        for i in range(col):
            s[0][i] = int(matrix[0][i])
        for i in range(1, row):
            s[i][0] = int(matrix[i][0])


        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    s[i][j] = min(s[i-1][j], s[i][j-1], s[i-1][j-1]) + 1
        
        _max = 0
        for i in range(row):
            for j in range(col):
                if s[i][j] > _max:
                    _max = s[i][j]
        return _max ** 2