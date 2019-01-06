## 31. Next Permutation
Permutation : Next smallest bigger number. <br />
To find next permutation, we first find the index that satisfy `nums[i] < nums[i+1]`. If there are no such index, means that there is no next permutation, because the `nums` in already in reverse sorted. Thus, the first index that has the above condition can make the next permutation. <br />
After we locate the index, next thing to do is find the smallest bigger element in `nums[i+1:]`, which index is j, then swap `nums[i], nums[j]`. After swapping, we then sort `nums[i+1:]`. What worth noting is that `nums[i+1:]` now is reverse ordered, thus we only need to reverse it again, then it's done. <br />
The reason that `nums[i+1:]` is from large to small is that we found the first element that satisfy the condition `nums[i] < nums[i+1]`. Thus those elements after i are already in reverse order. 
