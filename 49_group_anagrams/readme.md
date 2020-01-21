## 49. Group anagrams
### Description
Given an array of strings, group anagrams together.

Example:

```command
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

Note:
1. All inputs will be in lowercase.
2. The order of your output does not matter.

### Solution
Hash the sorted string, this takes O(NM*logM).
Or, we can hash the number of each character.