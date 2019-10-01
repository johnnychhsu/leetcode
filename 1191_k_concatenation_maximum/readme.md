## 1911. k-concatenation maximum
### Description
Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

```
Example 1:
    Input: arr = [1,2], k = 3
    Output: 9

Example 2:
    Input: arr = [1,-2,1], k = 5
    Output: 2

Example 3:
    Input: arr = [-1,-2], k = 7
    Output: 0
```

### Solution
Consider four cases.
1. The maximum subarray when k = 1
2. Sum of the array multiplied by `k`.
3. Sum of maximum prefix and suffix.
4. Sum of maximum prefix and suffix and sum of array multiplied by `k-2`.
