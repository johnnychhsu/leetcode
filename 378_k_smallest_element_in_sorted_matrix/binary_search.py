class Solution:
    def kthSmallest(self, matrix, k):
        N = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        
        while l <= r:
            mid = (l + r)>>1
            high = N - 1
            count = 0
            for row in range(N):
                while high > -1 and matrix[row][high] > mid:
                    high -= 1
                count += high + 1
            
            if count >= k :
                r = mid - 1
            else:
                l = mid + 1
        return l
