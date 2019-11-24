## 576. Out of boundary paths
### Description
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

### Solution
Dynamic programming. The initial condition is `dp[i][j] = 1`, because we are already there, thus the total path to `(i, j)` is 1. Then we start to iterate `N` times for each cell in the grid. What's worth note is that we can reduce the dp array from `3d` to `2d`, because every iteration we only need the previous state, thus we can only maintain a `2d` array in each interation in range of `N`. Remember to update hte dp array after each iteration. 
