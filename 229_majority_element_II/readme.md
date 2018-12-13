### 229. Majority Element II
#### Algorithm
Boyer-Moore Algorithm. The algorithm can find the majority element in an array in two pass O(n) time.  
In the first stage, do the following:  
```python
candidate = 0
count = 0
for n in nums:
    if count == 0:
        candidate = n
        count = 1
    elif n == candidate:
        count += 1
    else:
        count -= 1
```
Then the candidate would be the majority element if the majority exist. Thus, in the second stage (second pass), check the number of the candidates : 
```python
nums.count(candidate) > len(nums) // 2 + 1
```
#### This problem
This problem asks to find all elements that appear more than [n/3].  
There are at most 2 element can be, thus we maintain two candidates and two counters for each candidate.

#### Ref
https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
