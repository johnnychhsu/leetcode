## 525. Contiguous array
### Description
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example
```command
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
``` 

### Solution
We can utilize hash map. We first convert `0` into `-1`, then start to calculate the prefix sum from head of the array to the end.

The key idea is that we use a hash map to store the current sum `_sum` and corresponding index `i`. If we encounter the same `_sum` in different index, that means we have a contiguous sub-array between those two index. This sub-array is what we are looking for.
