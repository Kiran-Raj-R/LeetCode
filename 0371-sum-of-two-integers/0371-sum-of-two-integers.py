class Solution:
    def getSum(self, a: int, b: int) -> int:
        for i in range(abs(b)):
            if b > 0:
                a += 1
            else:
                a -= 1
        return a