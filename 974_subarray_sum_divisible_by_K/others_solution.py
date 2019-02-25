class Solution:
    def subarraysDivByK(self, A: 'List[int]', K: 'int') -> 'int':
        prefix = [0] * K
        prefix[0] = 1
        s = 0
        ans = 0
        for n in A:
            s = (s + n) % K
            s = s + K if s < 0 else s
            ans += prefix[s]
            prefix[s] += 1
        return ans
        
        
        
