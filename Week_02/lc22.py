class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S,left,right):
            if len(S) == 2*n:
                ans.append(S)
                return 
            if left < n:
                S += '('
                backtrack(S,left+1,right)
                S = S[:-1]
            
            if left > right:
                S += ')'
                backtrack(S,left,right+1)
            
        backtrack("", 0, 0)
        return ans
