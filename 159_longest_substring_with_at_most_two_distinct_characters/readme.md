### 159. Longest Substring with At Most Two Distinct Characters
1. All this kind of problems can be solved by two pointers(sliding window) method.

2. Use a dict to memory each encounter element's left-most position. If there are more than two elements in the dict, remove th left most one, set the left pointer to the removed one's position + 1. Then we can get the length of the sub-string.
