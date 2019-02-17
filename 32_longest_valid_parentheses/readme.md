## 32. Longest Valid Parentheses
We can still use dp to solve this. The subproblem will be longest parentheses that ends with index `i`, not longest till index `i`.
<br />
We can solve this problem in constant space. <br />
Consider forward and backward pass. For forward, `(` must appear before `)`, thus those invalid `)` will be all at the left of `(`. Thus we can calculate the number of `(` and `)` to find the valid length.
