class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if sum(range(maxChoosableInteger+1)) < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        
        dp = {}
        
        def find(used, target):
            if target <= 0:
                return False
            
            if used[-1] >= target:
                return True
            
            key = ''.join(map(str, used))
            if key in dp:
                return dp[key]
            
            for i in range(1, len(used)):
                if not find(used[0: i] + used[i+1:], target - used[i]):
                    dp[key] = True
                    return True
            dp[key] = False
            return False
        
        return find(list(range(maxChoosableInteger+1)), desiredTotal)
