class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack and s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
        max_l = 0
        if not stack:
            return len(s)
        else:
            if stack[0] == 0:
                prev = 0
            else:
                prev = -1
            for index in stack:
                max_l = max(max_l, index - prev - 1)
                prev = index
            max_l = max(max_l, len(s) - 1 - prev)
            return max_l
