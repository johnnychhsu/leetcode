## 844. Backspace String Compare
This can be solve in O(n). If we start from the end of the string, we know that the current character should be the same. If we encounter a `#`, we know we should skip the next character. 
<br />
The trick is that we treat `S` and `T` in separate while loop. We keep backwarding till there is no `#` or we run out of the cumulative `#`. Then we can chcek whether current characters are the same.
<br />
What worth noting is that, for the checking condition, we can use
```python
if not (s >= 0 and t >= o and S[s] == T[t]):
    return t == s == -1
``` 
The key point is that we can use `t == s == -1` to return True and False according the actual condition. <br />
For example, if one string finish earlier than another, then they are different and `s` and `t` would be different. <br />
If they both end at `s == t == 0`, which means that they are the same, then this condition will return True.
