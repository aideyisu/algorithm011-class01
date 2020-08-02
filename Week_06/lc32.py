# 32 最长有效括号
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result, current = 0, 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)
        return result
