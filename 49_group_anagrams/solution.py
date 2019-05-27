class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(s):
            return ''.join(sorted(s))
        
        ans_key = {}
        for s in strs:
            key = getKey(s)
            if key in ans_key:
                ans_key[key].append(s)
            else:
                ans_key[key] = [s]
        return [ans for ans in ans_key.values()]