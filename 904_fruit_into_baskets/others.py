import pdb


class Solution:
    def totalFruit(self, tree):

        prev, curr = [None, 0], [None, 0]
        res = 0

        for t in tree:
            pdb.set_trace()
            if t == curr[0]: curr[1] += 1
            else:
                prev, curr = curr, prev
                if t == curr[0]: prev[1] += curr[1]
                else: res = max(res, prev[1] + curr[1])
                curr = [t, 1]
                
        return max(res, prev[1] + curr[1])
sol = Solution()
sol.totalFruit([0,1,6,6,4,6,4])
