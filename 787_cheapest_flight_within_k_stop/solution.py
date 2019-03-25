class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        from collections import defaultdict
        record = defaultdict(list)
        for flight in flights:
            s, e, cost = flight
            if s in record:
                record[s].append((e, cost))
            else:
                record[s] = [(e, cost)]

        import heapq
        res = []
        heapq.heappush(res, (0, 0, src))
        while res:
            cost, times, cur = heapq.heappop(res)
            if cur == dst:
                return cost
            if times > K:
                continue
            else:
                for n in record[cur]:
                    heapq.heappush(res, (n[1] + cost,  times + 1, n[0]))
        return -1

