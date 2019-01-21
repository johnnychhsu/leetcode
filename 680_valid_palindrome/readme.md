## 680. Valid Palindrome II
We can check from head and tail. If we encounter a char that doesn't satisfy the palindrome rule, say index i, then we only need to check `s[i+1,j]` and `s[i, j-1]` two cases whether one of them is palindrome.
