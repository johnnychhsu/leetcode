## 1235. Maximum profit in job scheduling
### Description
We have n jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`.

Given startTime, endTime, profit, we need to output the maximum profit we can make such that there are no 2 jobs in the subset with overlapping time range

###Solution
Dynamic programming : first sort these jobs with endTime. This is like knapsack problem. We either take a job and see whether is larger or smaller. The key point is to find the right index to insert the job. We can do binary search in our `dp` array to find the right place for current job. We take the previous `dp` element, add the profit, then compare the result with the last `dp` element. If the result is larger, then we should take this job, and update the last element accordinglly.
