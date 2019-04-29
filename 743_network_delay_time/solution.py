class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        import heapq
        from collections import defaultdict
        time_map = defaultdict(list)
        for t in times:
            u, v, w = t
            time_map[u].append((w, v))
        res = []
        heapq.heappush(res, (0, K))
        visited = [0] * N
        time_req = [0] * N
        while res:
            t, cur = heapq.heappop(res)
            time_req[cur-1] = t
            if not visited[cur-1]:
                visited[cur-1] = 1
                for n in time_map[cur]:
                    _t, v = n
                    if not visited[v-1]:
                        heapq.heappush(res, (_t + t, v))
                if all(visited[i] == 1 for i in range(N)):
                    return max(time_req)
        return -1
            
