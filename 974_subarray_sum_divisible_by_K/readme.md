## 974. Subarray Sum Divisible by K
1. Prefix sum with map (or array) : Let `P = [0, A[0], A[0] + A[1], ...]` be the prefix sum array. Then when `P[i] == P[j]` , it means that `sum(A[i+1: j]) % K == 0`.
<br />
Why ? <br />
Let's say P[i] = a + r<sub>a, P[j] = b + r<sub>b, then <br />
```
P[j] - P[i] = b - a + rb - ra = K*c + (rb - ra)
```
Thus, when r<sub>b == r<sub>a, then `P[j] - P[i] % K == 0`.

