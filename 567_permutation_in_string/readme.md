## 567. Permutation in String
We can maintain an array length 26, record `s1` and `s2`'s word frequency. Then we keep a variable `count`. Each time encounter a new element, we campare the frenquency for `s1` and `s2`. If there is a match, we increase `count` by 1. If the leftest element's frenquency mismatch after decrease, then we decrease `count` by 1. If there is no match previous, then we don't need to consider it.
<br />
The point is that if there is a match, then all the 26 letters frenquency will match, then we can return `True`.
