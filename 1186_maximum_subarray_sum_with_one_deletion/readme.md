## 1186. Maximum subarray sum with one deletion
### Description
Given an array of integers, return the maximum sum for a non-empty subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be non-empty after deleting one element.

```
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
```

### Solution
1. Consider how to solve this without deletion. We can use Kadane’s algorithm. Keep the max accumulated so far, and the keep adding `a[i]` if the result is still positive.
