import pdb


class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        number = {}
        for i in range(len(nums)):
            max_l = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    max_l = max(max_l, dp[j] + 1)
            dp[i] = max_l

            if max_l == 1:
                if i in number:
                    number[i] += 1
                else:
                    number[i] = 1
            else:
                to_count = [index for index, _ in enumerate(dp[0: i]) if dp[index] == max_l - 1]
                for index in to_count:
                    if nums[i] > nums[index]:
                        if i in number:
                            number[i] += 1
                        else:
                            number[i] = number[index]
        _max = max(dp)
        ans = 0
        count_ans = [index for index, x in enumerate(dp) if x == _max]
        for num in count_ans:
            ans += number[num]
        return ans
        

sol = Solution()
test = [2,2,2,2,2]
test_1 = [3,1,2]
test_2 = [1,2,4,3,5,4,7,2]
a = sol.findNumberOfLIS(test_2)
print (a)



