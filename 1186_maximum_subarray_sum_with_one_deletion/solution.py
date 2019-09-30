class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        maxEndHere = [0 for _ in range(len(arr))]
        maxStartHere = [0 for _ in range(len(arr))]
        maxEndHere[0] = arr[0]
        maxStartHere[-1] = arr[-1]
        _max = arr[0]
        
        for i in range(1, len(arr)):
            maxEndHere[i] = max(maxEndHere[i-1] + arr[i], arr[i])
            _max = max(_max, maxEndHere[i])
        
        for i in range(len(arr)-2, -1, -1):
            maxStartHere[i] = max(maxStartHere[i+1] + arr[i], arr[i])

        for i in range(1, len(arr)-1):
            _max = max(_max, maxEndHere[i-1] + maxStartHere[i+1])
        return _max
            
