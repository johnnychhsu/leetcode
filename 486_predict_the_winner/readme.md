## 486. Predict the winner
Typical DP problem (this is also a minmax problem). Each player take turn choose the number, when the first player chooses, we want the maximum, while the second player chooses, we want to make sure player 2 has the minimum choice eben though player 2 chooses the maximum he can choosed.

### Description
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.
<br />
Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

### Reference
1 [MIT Design and Analysis of Algorithm](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/index.html)
