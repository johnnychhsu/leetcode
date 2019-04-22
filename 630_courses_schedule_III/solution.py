class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        import heapq
        pq = []
        start = 0
        courses.sort(key=lambda x: x[1])
        for t, end in courses:
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)

