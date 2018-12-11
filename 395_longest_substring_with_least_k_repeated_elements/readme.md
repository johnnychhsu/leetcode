### 395. Longest Substring with at least K Elements
#### First solution - 2 pointer sliding window 
Brute force check 26 different characters. Slides 2 pointer through the whole string, check whether there exist h unique character at least k times for each h in a~z.
  
The idea is that exhaustly search all possible unique character set that satisfy the at least k requirements. The reason we need to check all 26 possible set is that we don't know whether to move the pointer or not. So we need to set a limit there to tell whether we should keep exploring or we should move the right pointer forward, which is move the sliding window forward.
