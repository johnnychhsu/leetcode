import pdb


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def arange(cur_list):
            cur_list.sort(reverse=True)
            cur_ans = ''
            left = []
            for num in cur_list:
                if num % 10 != 0:
                    cur_ans += str(num)
                else:
                    left.append(num)
            for i in range(len(left) - 1, -1, -1):
                cur_ans += str(left[i])
            return cur_ans
            
        num_map = {}
        def classify(num):
            while num >= 10:
                num //= 10
            return num
        
        for num in nums:
            cla = classify(num)
            if cla in num_map:
                num_map[cla].append(num)
            else:
                num_map[cla] = [num]
        
        ans = ''
        
        for key in range(9, 0, -1):
            cur_list = num_map.get(key)
            if cur_list:
                ans += arange(cur_list)
        return ans
                
sol = Solution()
test = [10, 2]
test_1 = [12, 121]
a = sol.largestNumber(test_1)
print (a)
