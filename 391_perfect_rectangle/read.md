### 391. Perfect Rectangles
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.
  
Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

  
There two contraints. First is that the rectangles should not overlap. Second is that there must be no hole in the rectangles.
  
We can get the max area and compare to the sum of all the rectangles. If not equals, then return False.  
We can use the four corners of all the rectangles to tell whether there are overlaps or not.
