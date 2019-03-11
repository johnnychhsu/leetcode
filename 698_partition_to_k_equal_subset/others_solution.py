class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        
        s = sum(nums)
        target = s // k
        nums.sort(reverse=True)

        subset = [0] * k
        
        def find(i):
            if i == len(nums):
                if len(set(subset)) == 1:
                    return True
                return False
            else:
                for j in range(k):
                    subset[j] += nums[i]
                    if subset[j] <= target and find(i+1):
                        return True
                    subset[j] -= nums[i]
                    if subset[j] == 0:
                        break
                return False
        return find(0)
                        
        

