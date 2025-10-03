class Solution:
    def climbStairs(self, n: int) -> int:
        # s,m = 1,1
        # for i in range(n-1):
        #     s = s + m
        #     m = s - m
        # return s
        
        if n <= 2:
            return n

        prev, curr = 1, 1   # prev = ways(n-2), curr = ways(n-1)
        for i in range(n-1):
            temp = curr
            curr = curr + prev   # ways(i) = ways(i-1) + ways(i-2)
            prev = temp          # shift forward
        return curr
