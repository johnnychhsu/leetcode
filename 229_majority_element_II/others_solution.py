class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        limit = len(nums) // 3 + 1
        unique = len(nums) // limit # at most two elements
        candidate_1 ,candidate_2 ,count_1 ,count_2 = 0, 0, 0, 0
        
        if not nums:
            return []
        
        for n in nums:
            if n == candidate_1:
                count_1 += 1
            elif n == candidate_2:
                count_2 += 1
            elif count_1 == 0:
                candidate_1, count_1 = n, 1
            elif count_2 == 0:
                candidate_2, count_2 = n, 1
            else:
                count_1 -= 1
                count_2 -= 1
        ans = []
        for n in [candidate_1, candidate_2]:
            if nums.count(n) >= limit and n not in ans:
                ans.append(n)
        return ans
        
        
        
        
        
