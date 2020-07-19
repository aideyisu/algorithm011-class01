# 回溯算法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
                return
            
            if left < n:
                s += '('
                backtrack(s, left+1, right)
                s = s[:-1]
            
            if left > right:
                s += ')'
                backtrack(s, left, right+1)
        
        backtrack("", 0, 0)
        return ans
