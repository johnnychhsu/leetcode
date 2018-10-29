# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x.start)
        ans = []
        cur_inter = intervals[0]
        for interval in intervals[1:]:
            if interval.start <= cur_inter.end:
                cur_inter.end = max(interval.end, cur_inter.end)
            else:
                ans.append(cur_inter)
                cur_inter = interval
        ans.append(cur_inter)
        return ans
