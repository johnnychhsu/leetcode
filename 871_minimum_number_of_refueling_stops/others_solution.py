class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (distance, gas) in enumerate(stations):
            for t in range(i, -1, -1):
                if distance <= dp[t]:
                    dp[t+1] = max(dp[t+1], dp[t] + gas)
        for i, dis in enumerate(dp):
            if dis >= target:
                return i
        return -1
