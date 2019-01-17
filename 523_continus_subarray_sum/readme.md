## 523. Continuous Subarray Sum 
We can use hashmap to solve this problem in O(n). <br />
We go through the list, calculate the cumulative sum, and mod by k. If there is an index `i` that `cumulative sum % k` equals `m`, and another index `j` also has the same value. This implies that the sum of the array elements between `i` and `j` mod `n*k` equals 0.
