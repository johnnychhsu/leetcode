class Solution:
    def checkInclusion(self, s1: 'str', s2: 'str') -> 'bool':
        l = len(s1)
        left = 0
        word = {}
        import copy
        for w in s1:
            if w in word:
                word[w] += 1
            else:
                word[w] = 1
        while left + l <= len(s2):
            record = word.copy()
            for i in range(left, left + l):
                if s2[i] not in word or record[s2[i]] <= 0:
                    left += 1
                    break
                else:
                    record[s2[i]] -= 1
            if i == left + l - 1:
                return True
        return False                    
            
