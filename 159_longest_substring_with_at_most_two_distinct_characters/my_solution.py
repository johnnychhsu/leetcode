class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = cur = 0
        _max = 0
        visited = []
        limit = 2
        
        while right < len(s):
            if s[right] in visited:
                right += 1
            else:
                if len(visited) < limit:
                    visited.append(s[right])
                    right += 1
                else:
                    target = s[right - 1]
                    _max = max(_max, right - cur)
                    visited = [target]
                    while left < right:
                        if s[left] == target:
                            left += 1
                        else:
                            left += 1
                            cur = left
                    left = cur
        _max = max(_max, right - cur)
        return _max
                        
                            
                    
                    
                    
