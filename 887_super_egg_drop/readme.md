## Super egg drop
The state is `dp(k, n)`, `k` is number of eggs and `n` is the level of stairs. <br />
The optimal drop stair is not necessary the middle floor, thus we need to check `x for x from 1 to n` cases. This is the basic dp solution idea. <br />

We can improve this solution. Note that the solution `max(dp[x-1], dp[n-x])`, the second term increase with respect to n. Thus, we don't need to check for all x from 1 to n, we can start the checking from the last optimal `x`.
