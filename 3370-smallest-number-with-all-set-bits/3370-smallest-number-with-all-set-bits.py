class Solution:
    def smallestNumber(self, n: int) -> int:
        t = 2
        for i in range(11):
            if t ** i > n:
                return (t ** i) - 1