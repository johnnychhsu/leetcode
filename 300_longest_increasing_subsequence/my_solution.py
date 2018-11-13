"""
This is O(n^2)
"""
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def find(nums, pre_num, cul):
            if not nums:
                return cul
            else:
                cur_max = 0
                if nums[0] > pre_num:
                    cur_max = max(find(nums[1:], nums[0], cul + 1), find(nums[1:], pre_num, cul))
                else:
                    cur_max = find(nums[1:], pre_num, cul)
                
                return cur_max
        
        _max = 0
        for i in range(len(nums)):        
            _max = max(find(nums[i:], -2**16, 0), _max)
        return _max
        
        
sol = Solution()   

b = [1,2]
c = [1,3,6,7,9,4,10,5,6]
a = sol.lengthOfLIS(c)
print (a)
