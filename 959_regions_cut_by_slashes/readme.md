## 959. Regions cut by slashes
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.
<br />
(Note that backslash characters are escaped, so a \ is represented as "\\".)
<br />
Return the number of regions.
<br />

Example:
```command
Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:
```
![example](example.png)

### Solution
We need to convert the slashes string into another map, so that we can count the regions. To do this, we can extend the slashes into 3 times larger, that is, extend the `1x1` square into `3x3` square. In this extended map, we can express the slashes with regions cut by them. Note that a `2x2` square is too 'thick' to express the regions. Think about this case :
![example2](example2.png)
