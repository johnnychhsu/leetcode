class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def helper(l, r):
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return s[l+1: r]
        tmp = ''
        for i in range(len(s)):
            l1 = helper(i,i)
            l2 = helper(i, i+1)
            if len(l1) > len(l2):
                if len(l1) > len(tmp):
                    tmp = l1
            else:
                if len(l2) > len(tmp):
                    tmp = l2
        return tmp
                    
