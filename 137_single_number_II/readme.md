## 137. Single number II
### Description
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#### Example
```command
Input: [2,2,3,2]
Output: 3
```

### Solution
Use 2 bits so store the number state. Suppose we have 2 bits `ab = 00`. If we have one number called `n`, we can store this unformation like `ab = 01`. Suppose now we encounter second `n`, `ab` should become `10` to represent that we have 2 `n` in total.

Now think about we encounter the third `n`. `ab` should become `00` because we want to remove all numbers appear three times, and keep the number that only appears once. 

To achieve that, we can keep `a`, `b` as follow : 
```python
# Initial state
a = 0
b = 0

# Update rule
b = b ^ n & ~a
a = a ^ n & ~b
```
Why? Consider when should `a` and `b` become one or zero. `b` should become one when we meet `n` the first time. Then second and third time, `b` should be zero.


`a` should become one when we encounter `n` the second time. When the third comes, we should turn `a` into zero, and also `b`. Thus, we need `~a` and `~b` to achieve this.
