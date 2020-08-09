# 这道题作为DP动态规划经典题目,入门是很厉害的
# 因为每一级台阶等于前两级台阶的和,所以
# DP[i] = DP[i - 1] + DP[i - 2]

class Solution:
    def climbStairs(self, n: int) -> int:
        a , b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b
