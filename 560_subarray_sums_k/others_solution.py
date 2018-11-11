class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        acu = 0
        ans = 0
        cache = {0:1}
        for num in nums:
            acu += num
            if acu - k in cache:
                ans += cache[acu - k]
            if acu in cache:
                cache[acu] += 1
            else:
                cache[acu] = 1
        return ans
                
        
                
        
