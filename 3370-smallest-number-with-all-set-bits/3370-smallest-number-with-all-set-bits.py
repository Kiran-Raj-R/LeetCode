class Solution:
    def smallestNumber(self, n: int) -> int:
        t = 2
        if n == 1:
            return 1
        for i in range(11):
            if t ** i > n:
                return (t ** i) - 1