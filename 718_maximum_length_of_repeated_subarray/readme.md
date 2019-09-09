## 718. Maximum length of repeated subarray
### Problem
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
```
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
```

### Solution
Dynamic programming. The key point is that we use a 2 dimension array to store the repeated subarray. What's worth noting is that we use `dp[i][j]` to store the repeated subarray length of `A[i:]` and `B[j:]`.
