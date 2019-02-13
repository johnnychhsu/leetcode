## 713. Subarray product less than k
Use a sliding window concept, each time multiply one item to the current product. If it is less than k, then add all subarray that contains the newest element. If larger or equal than k, then divide the rightest element till the current product less than k. <br />

### Algorithm

Our loop invariant is that left is the smallest value so that the product in the window prod = nums[left] * nums[left + 1] * ... * nums[right] is less than k.
<br />
For every right, we update left and prod to maintain this invariant. Then, the number of intervals with subarray product less than k and with right-most coordinate right, is right - left + 1. We'll count all of these for each value of right.
