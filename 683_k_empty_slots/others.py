class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        days = [0] * (len(flowers) + 1)
        for index, f in enumerate(flowers):
            days[f] = index + 1
        left = 1
        right = left + k + 1
        i = 1
        res = float('inf')
        while right < len(days):
            if days[i] < days[left] or days[i] <= days[right]:
                if i == right:
                    res = min(res, max(days[left], days[right]))
                left = i
                right = left + k + 1
            i += 1
        if res == float('inf'):
            return -1
        else:
            return res
