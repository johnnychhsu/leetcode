class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        from collections import defaultdict
        sum_map = defaultdict(int)
        _sum = 0
        ans = 0
        for n in A:
            _sum += n
            if _sum == S:
                ans += 1
            if _sum - S in sum_map:
                ans += sum_map[_sum-S]
            sum_map[_sum] += 1
        return ans