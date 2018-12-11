class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = len(s)
        _max = 0
        # Check all 26 characters
        for limit in range(1, 27):
            counter = [0] * 26
            left = right = unique = no_less_than_k = 0
            while left < l:
                if unique <= limit:
                    index = ord(s[left]) - ord('a')
                    if counter[index] == 0:
                        unique += 1
                    counter[index] += 1
                    if counter[index] == k:
                        no_less_than_k += 1
                    left += 1
                else:
                    index = ord(s[right]) - ord('a')
                    if counter[index] == k:
                        no_less_than_k -= 1
                    counter[index] -= 1
                    if counter[index] == 0:
                        unique -= 1
                    right += 1
                if unique == no_less_than_k:
                    _max = max(_max, left - right)
                    
        return _max
        
        
