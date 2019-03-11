## 698. Partition to k equal sum subset
This is a backtracking problem. <br />
We need to check all possible combination, with some tricks to avoid repeated check. Below are some tips : 
1. We need to find `k` groups that sums to `sum(nums) / k`.
2. So we can add each element in to `k` groups, and check whether this operation satisfy the limit `sum(subset[j] <= target)`.
3. If so, then we can recursively check next element, each call we iteratively add it to all subset and check.
4. What worth noting, if there is a subset that equals to 0 after we remove the added element, say `subset[j] - nums[i] == 0`, which means that this combination will not work since all the left subset is 0 (because we always start from the first subset), thus we can break the loop and go to the nextrecursive call. 
