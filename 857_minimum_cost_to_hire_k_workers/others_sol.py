class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        ratios = sorted([(w/q, q) for w, q in zip(wage, quality)], key=lambda x: x[0])
        import heapq
        workers = []
        q_sum = 0
        min_wage = float('inf')
        for ratio, q in ratios:
            heapq.heappush(workers, -q)
            q_sum += q
            if len(workers) == K:
                min_wage = min(min_wage, q_sum * ratio)
            if len(workers) > K:
                q_sum += heapq.heappop(workers)
                min_wage = min(min_wage, q_sum * ratio)
        return min_wage
