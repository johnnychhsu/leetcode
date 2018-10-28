class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_end, cur_farest, step = 0, 0, 0
        l = len(nums)
        for i, num in enumerate(nums[: l-1]):
            cur_farest = max(cur_farest, i + nums[i])
            if i == cur_end:
                step += 1
                cur_end = cur_farest
        return step
                
            
