## 139. Word Break
Dynamic programming : The original string can be separated into s1 and s2, two sub-string. If both sub-string satisfy, that is both in the dict, then s satisfy. <br />
So we construct a dp array length `n+1`, and init `dp[0]=True` because empty string is always in the dict. Then, we use two pointer, `i` and `j`, `s[0:j+1]` and `s[j+1:i+1]` as s1 and s2. If `dp[j]` is True, then we check whether `s[j+1:i+1]` is in teh dict or not. <br />
If it is in the dict, then we set `dp[i]` to True. 
