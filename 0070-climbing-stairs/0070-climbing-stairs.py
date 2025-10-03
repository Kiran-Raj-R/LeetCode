class Solution:
    def climbStairs(self, n: int) -> int:
        s,m = 1,1
        for i in range(n-1):
            s = s + m
            m = s - m
        return s