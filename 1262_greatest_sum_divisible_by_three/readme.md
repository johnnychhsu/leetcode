## 1262. Greatest sum divisible by three
### Description
Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

```
Example 1:

Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
```

### Solution
We can have a solution with time O(n) and space O(1). Simply go through every element and record current maximum sum with reminder `0, 1, 2`. Add the current element to each reminder and update the corresponding reminder record.
