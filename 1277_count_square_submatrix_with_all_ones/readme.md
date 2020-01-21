## 1277. Count square submatrix with all ones
### Description
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

```
Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

### Solution
1. Dynamic programming
We can use `dp[x][y]` representing the total number of squares with `(x, y)` as its bottom-right coordinate.
