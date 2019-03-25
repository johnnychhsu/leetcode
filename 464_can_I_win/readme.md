## 464. Can I Win
### Description
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.
<br />
What if we change the game so that players cannot re-use integers?
<br />
For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
<br />
Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.
<br />
You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

### Solution
We can use dynamic programming. The key point is to used the left choosable number as key to memorize the sub-problem result.
