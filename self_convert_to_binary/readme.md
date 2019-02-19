## Convert to Binary
Loop Invariant : 
```python
n = tmp * (2 ^ i) + sigma(A[i] * (2 ^ i))
```
1. First, prove that this loop invariant holds for the init condition
2. Second, prove that after the loop exit, this invariant still holds
3. Finally, use induction to prove the invariant holds for every interation. Check changing variables for proof. For example, `i` and `tmp` and `A[i]`. It is like : 
```python
i' = i + 1
tmp' = tmp // 2
n' = n
A[k] >= 0 for all k >= i
A[k] are all the same except for k == i
```
