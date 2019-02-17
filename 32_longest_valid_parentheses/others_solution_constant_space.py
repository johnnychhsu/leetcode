class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        openc,prevV,res,maxl = 0,0,0,0
        for c in s:
            if c=='(': openc += 1
            elif openc:
                openc -= 1
                res += 2
                if not openc:
                    prevV += res
                    res = 0
                    maxl = max(prevV,maxl)
            else: res,prevV = 0,0
        openc,prevV,res = 0,0,0
        for c in s[::-1]:
            if c==')': openc += 1
            elif openc:
                openc -= 1
                res += 2
                if not openc:
                    prevV += res
                    res = 0
                    maxl = max(prevV,maxl)
            else: res,prevV = 0,0
        return maxl
