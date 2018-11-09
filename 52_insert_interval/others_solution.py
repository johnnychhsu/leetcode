class Solution(object):
    def insert(self, intervals, newInterval):
        i = 0
        res = []
        
        # skip smaller parts
        while i < len(intervals) and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        
        # merge
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            i += 1
        res.append(newInterval)         # !!!
        
        # add the rest
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res
