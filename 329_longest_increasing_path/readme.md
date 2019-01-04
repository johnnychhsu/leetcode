## 329. Longest Increasing Path
### DFS with memorization
**Problem** <br />
Given an integer matrix, find the length of the longest increasing path.
<br />
From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

<br />

We can do dfs for each cell in this matrix. This naive solution is O(2^(m+n)). Because we calculate duplicate problems many times, thus we need to cache them.
<br />
The idea is dynamin programming with dfs. We use a matrix to memorize the calculation of each subproblems. So if there is a record for the subproblem, we can get the answer in O(1). So the time complexity reduce to O(mn).
