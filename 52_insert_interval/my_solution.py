# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def isOverlap(inter_1, inter_2):
            if inter_2.start <= inter_1.start <= inter_2.end:
                return True
            if inter_2.start <= inter_1.end <= inter_2.end:
                return True
            if inter_1.start <= inter_2.start <= inter_1.end:
                return True
            if inter_1.start <= inter_2.end <= inter_1.end:
                return True
        
        new_s = newInterval.start
        new_e = newInterval.end
        
        new_inter = Interval()
        to_remove = set()
        lock = 0
        
        if not intervals:
            return [newInterval]
        
        for i in range(len(intervals)):
            if isOverlap(newInterval, intervals[i]):
                if lock == 0:
                    if intervals[i].end >= new_s:
                        if intervals[i].start < new_s:
                            new_inter.start = intervals[i].start
                        else:
                            new_inter.start = new_s

                        if intervals[i].end > new_e:
                            new_inter.end = intervals[i].end
                        else:
                            new_inter.end = new_e
                        if new_inter.start == intervals[i].start and new_inter.end == intervals[i].end:
                            return intervals
                        lock = 1
                        to_remove.add(i)
                if lock == 1:
                    if intervals[i].start > new_inter.end:
                        break
                    else:
                        if intervals[i].end >= new_inter.end:
                            new_inter.end = intervals[i].end
                            to_remove.add(i)
                            break
                        to_remove.add(i)
        if not to_remove:
            intervals.append(newInterval)
        else:
            remove_s = min(to_remove)
            remove_e = max(to_remove)
            intervals = intervals[0: remove_s] + intervals[remove_e + 1:]
            intervals.append(new_inter)
        intervals.sort(key = lambda x: x.start)
        return intervals
                        
                    
        
        
        
