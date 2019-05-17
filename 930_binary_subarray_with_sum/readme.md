## 930. Binary subarray with sum
### Description
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

```command
Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
```

### Solution
We can use a hash map to store prefix sum. So if suppose current prefix sum from index `o` to `i` equals `S`, then we find a matching subarray. Then we check whether there are some other prefix sum appeared previously equal to `S`. If yes, then the segment between current index and those previous index also match, we can add those into `ans`.