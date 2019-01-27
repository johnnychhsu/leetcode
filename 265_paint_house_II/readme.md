## 265. Paint House II
There are k colors for each house.

### Other's solution
What's difference from this question to the original 3 colors question is that, we don't need to find the min for all previous row, we simply need to track minimum and second minimum. If current row's minimum has the same index as previousm, then we use second minimum. This solution reduce the comparison times.
