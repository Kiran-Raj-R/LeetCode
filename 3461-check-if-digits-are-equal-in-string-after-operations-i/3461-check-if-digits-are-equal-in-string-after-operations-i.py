class Solution:
    def hasSameDigits(self, s: str) -> bool:
        d = [int(digit) for digit in s]
        while len(d) > 2:
            new = []
            for i in range(len(d) - 1):
                psum = d[i] + d[i+1]
                new.append(psum % 10)
            d = new
        return d[0] == d[1]