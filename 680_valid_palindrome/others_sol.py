class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def allright(l, r):
            return all(s[k] == s[r-k+i] for k in range(l, r))
        
        length = len(s)
        for i in range(0, length//2):
            if s[i] != s[length - 1 - i]:
                return allright(i+1, length-i) or allright(i, length-i-2)
        return True
