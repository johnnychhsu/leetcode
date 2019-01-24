## Coin Exchange
Given a number `n`, a list of coin `c`, determine how many ways are there to make the number using these coins. <br />
**Dynamic Programming** <br />
We can maintain a table `[[0 for x in range(len(c))] for i in range(n+1)]`. The problem can be separated as
```python
getWays(n, c, m) = getWays(n, c, m - 1) + getWays(n - c[m], c, m)
```
Using `mth` coin or not using `mth` coin. If we use, then `n - c[m]`, keep the whole coin list and check `n-c[m]`'s solution.
If we don't use, then check solution using `m-1` coins with the same `n`.
