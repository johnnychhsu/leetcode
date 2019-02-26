class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        i = 0
        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                h = heights[stack.pop()]
                left_i = stack[-1] if stack else -1
                ans = max(ans, h * (i - left_i - 1))

        while stack:
            h = heights[stack.pop()]
            left_i = stack[-1] if stack else -1
            print(ans)
            ans = max(ans, h * (i - left_i - 1))
        return ans
