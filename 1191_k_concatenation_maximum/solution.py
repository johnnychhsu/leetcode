class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        prefix = [0 for _ in range(len(arr))]
        suffix = [0 for _ in range(len(arr))]
        subarray = [0 for _ in range(len(arr))]
        prefix[0] = arr[0]
        suffix[-1] = arr[-1]
        subarray[0] = arr[0]
        for i in range(1, len(arr)):
            prefix[i] = arr[i] + prefix[i-1]
            subarray[i] = max(arr[i], arr[i] + subarray[i-1])
        for i in range(len(arr) - 2, -1, -1):
            suffix[i] = arr[i] + suffix[i+1]
        if k == 1:
            _max = max(subarray)
            return _max % (10**9 + 7) if _max > 0 else 0
        else:
            prefix_max = max(prefix)
            suffix_max = max(suffix)
            if prefix_max < 0:
                prefix_max = 0
            if suffix_max < 0:
                suffix_max = 0
            arrSum = sum(arr)
            candidate_1 = prefix_max + suffix_max
            candidate_2 = arrSum * k
            candidate_3 = prefix_max + suffix_max + arrSum * (k-2)
            _ans = max(candidate_1, candidate_2, candidate_3, max(subarray))
            return _ans % (10**9 + 7)
