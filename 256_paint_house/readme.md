## 256. Paint House
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color. <br />

### Example
```command
Input: [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
             Minimum cost: 2 + 5 + 3 = 10.
```

### My solution
1. Time : O(n)
2. Space : O(n)

### Other's solution
1. Time : O(n)
2. Space : O(1)
We don't have to memory all previous value, just the previous one row value and keep update it.
