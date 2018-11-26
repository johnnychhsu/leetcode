import pdb


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def sum_area(pairs, height):
            area = 0
            for pair in pairs:
                standard = min(height[pair[0]], height[pair[1]])
                for h in height[pair[0] + 1: pair[1]]:
                    if h < standard:
                        area += standard - h
            return area
        if not height:
            return 0
        prev_h = height[0]
        lock = 0
        left_h = 0
        right_h = 0
        mark = []

        for index, h in enumerate(height):
            if lock == 0 and h < prev_h:
                left_h = index - 1
                lock = 1
            if lock == 1 and h > prev_h:
                right_h = index
            if lock == 1 and h >= height[left_h]:
                right_h = index
                lock = 0
                mark.append((left_h, right_h))
                left_h = 0
                right_h = 0
            prev_h = h
        if lock == 1 and right_h != 0:
            mark.append((left_h, right_h))
        pdb.set_trace()
        area = sum_area(mark, height)
        return area
    
sol = Solution()
test = [9,6,8,8,5,6,3]
a = sol.trap(test)
print (a)
