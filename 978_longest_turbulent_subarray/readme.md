## 978. Longest Turbulent Subarray
A subarray `A[i], A[i+1], ..., A[j]` of `A` is said to be turbulent if and only if:
1. For `i <= k < j, A[k] > A[k+1]` when `k` is odd, and `A[k] < A[k+1]` when `k` is even
2. OR, for `i <= k < j, A[k] > A[k+1]` when `k` is even, and `A[k] < A[k+1]` when `k` is odd.
