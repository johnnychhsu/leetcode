## 1187. Make Array Strictly Increasing
### Description
Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.

In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].

If there is no way to make arr1 strictly increasing, return -1.

**Example 1:**
 ```
Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
```

**Example 2:**
```
Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6, 7].
```

### Solution
This problem can be solved using dynamic programming. The key point is how to define the state and the transtion function.
We can maintain a `dp` dictionary, which use the element in `arr` as key, the number of operation (change with `arr2`) as the value. For each element in `arr1`, if it is larger than previous one, we can either change the element with `arr2`, or keep it there. If the element id smaller than the previous one, then we must change it. So, we need to keep all valid previous states in `dp`, and update the states in `dp` when iterationg through `arr1`. We only maintain valid state in `dp`, thus, after the final element is evaluated in the loop, we can know if there is a minimum number of operations that can make `arr1` strictly increasing.

### Lessons learned from this problem
DP can not only be a list for cache, and recursivly solving dp problems. The key idea is to define the state appropritely, then store the state accordingly. It is not necessary to use a list and index as state transition function. What really matters is how to keep the state for the overlapping subproblem.