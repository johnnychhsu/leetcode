class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxHere = 0
        minHere = 0
        maxPrev = nums[0]
        minPrev = nums[0]
        maxAll = nums[0]
        for n in nums[1:]:
            maxHere = max(maxPrev * n, minPrev * n, n)
            minHere = min(maxPrev * n, minPrev * n, n)
            maxAll = max(maxAll, maxHere)
            maxPrev = maxHere
            minPrev = minHere
        return maxAll
            
        
