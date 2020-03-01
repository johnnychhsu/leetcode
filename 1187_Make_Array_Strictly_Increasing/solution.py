class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        from collections import defaultdict
        import bisect
        arr2.sort()
        dp = {-1:0}
        for i in arr1:
            tmp = collections.defaultdict(lambda: float('inf'))
            for k in dp:
                if i > k:
                    tmp[i] = min(tmp[i], dp[k])
                _change_index = bisect.bisect_right(arr2, k)
                if _change_index < len(arr2):
                    tmp[arr2[_change_index]] = min(tmp[arr2[_change_index]], dp[k] + 1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1
