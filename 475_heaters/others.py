class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.append(float('inf'))
        heaters.sort()
        houses.sort()
        res = i = 0
        for house in houses:
            while house > (heaters[i] + heaters[i+1]) // 2:
                i += 1
            res = max(res, abs(house - heaters[i]))
        return res
