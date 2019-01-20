## 33. Search In Rotated Array
### Binary Search
The solution should be in O(n). First we binary search the rotate index. Then according to the target, we choose the correct half to do binary search for the target. <br />
When search for the rotate index, remember to handle cases likes `[], [1], [1,3,5]` which are null list, single element list or no rotate index cases. <br />
When shrinking the left and right pointer, remember to handle index out of range case, we can avoid this case by checking whetther there is rotate index first. If yes, then the binary search won't touch the edge case, which is the last element.
